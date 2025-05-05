"""
All blueprints imported in one module
"""

from flask import Blueprint

from dataclasses import dataclass

from .root.api import bp as root


@dataclass
class BlueprintWrapper:
    path: str
    blueprint: Blueprint


def all_blueprints() -> list[BlueprintWrapper]:
    return [
        BlueprintWrapper(path="", blueprint=root),
    ]
