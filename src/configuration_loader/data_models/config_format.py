from pathlib import Path
from typing import List, Union, Dict

ItemPropertiesFormat = Union[List[str], str]
ItemFormat = Dict[str, ItemPropertiesFormat]
ConfigFormat = Dict[str, List[ItemFormat]]
