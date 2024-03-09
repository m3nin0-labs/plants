#
# Copyright (C) 2024 Plants.
#
# Plants is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

from importlib import import_module

MODULES = [
    "plants.modules.config",
    "plants.modules.db",
    "plants.modules.validation",
    "plants.modules.security",
    "plants.modules.api",
]


def init_modules(app):
    """Initialize extensions modules."""

    for module in MODULES:
        mod = import_module(module)
        mod.init_module(app)
