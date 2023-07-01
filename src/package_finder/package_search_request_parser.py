from json import loads
from typing import Dict, Final, List, Union
from pathlib import Path
import os

from data_models.package_search_request import ParsedPackage
from data_models.configuration_path import ConfigurationPath


PackageDataFormat = Dict[str, Union[str, List[str]]]
PackageSearchRequestDictFormat = Dict[str, PackageDataFormat]


class PackageSearchRequestParser:
    __PACKAGE_GROUP_KEY: Final[str] = "package_group"
    __SEARCH_QUERY_KEY: Final[str] = "search_query"
    __EXPECTED_PACKAGE_DATA_KEYS: Final[List[str]] = [
        __PACKAGE_GROUP_KEY,
        __SEARCH_QUERY_KEY,
    ]

    def __init__(self) -> None:
        self.__package_configuration_path = self.__get_package_configuration_path()
        self.__package_search_requests = []
        self.__parse_package_search_requests_dict()

    @property
    def package_search_requests(self) -> List[ParsedPackage]:
        return self.__package_search_requests

    def __parse_package_search_requests_dict(self) -> None:
        search_request_dict = self.__load_package_search_request_file()
        for package_id, package_data in search_request_dict.items():
            if not self.__validate_package_search_request(package_id, package_data):
                continue

            self.__create_package_search_request(package_id, package_data)

    def __load_package_search_request_file(self) -> PackageSearchRequestDictFormat:
        with open(self.__package_configuration_path, "r", encoding="utf-8") as package_config_file:
            package_search_requests = package_config_file.read()
        return loads(package_search_requests)

    @staticmethod
    def __get_package_configuration_path() -> Path:
        src_path = Path(os.path.realpath(__file__)).parent.parent
        return src_path / ConfigurationPath.PACKAGE_CONFIGURATION_PATH.value

    def __validate_package_search_request(self, package_id: str, package_data: PackageDataFormat) -> bool:
        try:
            self.__validate_package_data_keys(package_data)
            self.__check_for_duplicate_package_ids(package_id)
        except KeyError as err:
            print(err)
            return False
        return True

    def __validate_package_data_keys(self, package_data: PackageDataFormat) -> None:
        for key in self.__EXPECTED_PACKAGE_DATA_KEYS:
            if key not in package_data:
                raise KeyError(
                    f"File {self.__package_configuration_path} is missing key {key} in section '{package_data}'"
                )

    def __check_for_duplicate_package_ids(self, package_id: str) -> None:
        package_search_request_names = [request.name for request in self.package_search_requests]
        if package_id in package_search_request_names:
            raise ValueError(f"File {self.__package_configuration_path} contains a key duplicate: '{package_id}'")

    def __create_package_search_request(self, package_id: str, package_data: PackageDataFormat) -> None:
        package_search_request = ParsedPackage(
            name=package_id,
            search_query=package_data[self.__SEARCH_QUERY_KEY],  # type:ignore
            package_group=package_data[self.__PACKAGE_GROUP_KEY],  # type:ignore
        )
        self.package_search_requests.append(package_search_request)


if __name__ == "__main__":
    print(PackageSearchRequestParser().package_search_requests)
