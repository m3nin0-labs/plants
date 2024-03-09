#
# Copyright (C) 2024 Plants.
#
# Plants is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Plants configuration module."""

from dynaconf import FlaskDynaconf


def init_module(app):
    """Initialize the ``Configuration`` module."""

    FlaskDynaconf(
        app,
        SETTINGS_FILE="settings.toml",
    )


__all__ = ("init_module",)
