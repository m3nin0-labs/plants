# Plants

The Plants API is a RESTful service designed to make illustrations of plants from old books available through the International Image Interoperability Framework (IIIF), leveraging the Invenio-IIIF library.

> **Note**: This is a hobby project.

## Features

- **Search plants illustrations (`/plants`)**: Users can access a list of available plants illustrations;

- **IIIF Image Retrieval (`/iiif`)**: Utilizes IIIF standards to serve images of plants, enabling rich interaction such as zooming and panning.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
- Git
- Make
- Docker and Docker Compose

### Installation (Docker)

To use the `Plants API`, first, you need to clone the repository:

```sh
git clone https://github.com/m3nin0-labs/plants
```

Then, navigate to the cloned directory:


```sh
cd plants
```

In the repository directory, use `make` to configure it. To do this, you can start the containers:

```sh
make up
```

Then, execute the database migrations:

```sh
make migrations
```

To populate the database with example data, use:

```sh
make ingest
```

Other options are available in the `Makefile`, including:

- `make up`: Start the application and database using Docker and Docker-compose;
- `make down`: Stop and remove containers, networks, images, and volumes;
- `make migrations`: Run database migrations to prepare your environment;
- `make ingest`: Ingest example data into the database to start testing the API.

## Development

To develop the `Plants API`, first, you need to clone the repository:

```sh
git clone https://github.com/m3nin0-labs/plants
```

Then, access the cloned repository:

```sh
cd plants
```

You can install the project using:

```sh
poetry install
```

After install the project, you can create a database (PostgreSQL). Before execute the command below, make sure the database address in the `settings.toml` is correct:

```sh
FLASK_APP=plants/main.py flask db upgrade
```

Then, you can execute the project:

```sh
FLASK_APP=plants/main.py flask run
```

## Contributing

We welcome contributions! If you have suggestions for improvements or bug fixes, please feel free to fork the repository and submit a pull request.

## Acknowledge

The example data available in this repository, comes from the [Old Book Illustrations](https://www.oldbookillustrations.com/) website. Thanks!

## License

`plants` is distributed under the MIT license. See LICENSE for more details.
