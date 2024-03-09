#
# Copyright (C) 2024 Plants.
#
# Plants is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

from flask import Flask

from plants.modules import init_modules


def create_app():
    """Create Plants application."""

    #
    # Creating app
    #
    app = Flask(__name__)

    #
    # Loading extensions
    #
    init_modules(app)

    return app


__version__ = "0.1.0"

__all__ = ("__version__", "create_app")
