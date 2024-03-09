#
# Copyright (C) 2024 Plants.
#
# Plants is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

workers = "4"
bind = "0.0.0.0:8000"

wsgi_app = "plants.main:app"
