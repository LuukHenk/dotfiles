

from typing import List

from data_models.package_search_request import PackageSearchRequest

def get_package_search_requests() -> List[PackageSearchRequest]:
    return [
        PackageSearchRequest(
            name="Neovim",
            search_query=["neovim", "nvim"],
            package_group="Neovim"
        ),
        PackageSearchRequest(
            name="Spotify",
            search_query=["spotify"],
            package_group="Spotify"
        )
    ]