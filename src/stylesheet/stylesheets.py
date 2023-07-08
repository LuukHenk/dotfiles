from typing import Dict

from stylesheet.sub_stylesheets.package_stylesheet import get_raw_package_stylesheet


class StyleSheets:
    def __init__(self):
        self.__default_stylesheet = self.__construct_stylesheet()
        self.__stylesheet_on_package_hover = self.__construct_stylesheet(package_hover=True)

    @property
    def default_stylesheet(self) -> str:
        return self.__default_stylesheet

    @property
    def stylesheet_on_package_hover(self) -> str:
        return self.__stylesheet_on_package_hover

    def __construct_stylesheet(self, package_hover: bool = False) -> str:
        stylesheet = ""
        stylesheet += self.__construct_stylesheet_from_raw(get_raw_package_stylesheet(package_hover))
        return stylesheet

    @staticmethod
    def __construct_stylesheet_from_raw(raw_stylesheet: Dict[str, Dict[str, str]]) -> str:
        stylesheet = ""
        for object_name, object_properties in raw_stylesheet.items():
            stylesheet += f"QWidget{object_name}" + " {\n"
            for key, value in object_properties.items():
                stylesheet += f"\t{key}: {value};\n"
            stylesheet += "}\n"
        return stylesheet
