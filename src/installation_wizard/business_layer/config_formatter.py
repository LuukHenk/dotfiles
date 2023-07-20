from typing import List, Dict

from data_models.item import Item


def format_by_groups(config: List[Item]) -> Dict[str, List[Item]]:
    groups = {}
    for config_item in config:
        group = groups.get(config_item.group, [])
        group.append(config_item)
        groups[config_item.group] = group
    return groups
