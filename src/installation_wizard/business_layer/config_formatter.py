from typing import List

from data_models.item import Item
from installation_wizard.data_models.installation_wizard_data_formats import ItemGroupsFormat


def format_by_groups(config: List[Item]) -> ItemGroupsFormat:
    groups = {}
    for config_item in config:
        group = groups.get(config_item.group, [])
        group.append(config_item)
        groups[config_item.group] = group
    return groups
