#
# Copyright (C) 2024 Plants.
#
# Plants is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

FROM python:3.9

# Working directory
WORKDIR /app

# Copy application
COPY . .

# Install dependencies
RUN pip install --no-cache-dir .

# Base application
CMD ["gunicorn", "-c", "gunicorn.config.py"]
