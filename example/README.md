
## Example Data Ingestion for Plants API

This directory contains scripts for ingesting example data into the Plants API database. The example data is sourced from [Old Book Illustrations](https://www.oldbookillustrations.com/), which provides a rich collection of high-quality, public domain illustrations from old books.

## Prerequisites
- Git
- Make
- Docker and Docker Compose
- Plants API repository setup with necessary Docker configurations.

## Using the Example Data

To use the example data:

1. Ensure that the Plants API is set up and that Docker and Docker-compose are installed and running on your system.
2. Navigate to the root directory of the Plants API project.

### Ingest Data

Run the following command from the root directory of your project to ingest the example data into the database:

```bash
make ingest
```

This command will execute the scripts located in this directory, which will populate your database with data from Old Book Illustrations suitable for use with the IIIF service.
