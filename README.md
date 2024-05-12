# Plants

The Plants API is a RESTful service designed to make illustrations of plants from old books available through the International Image Interoperability Framework (IIIF), leveraging the Invenio-IIIF library. This project aims to provide an accessible way to explore botanical illustrations with advanced image viewing capabilities.

> **Note**: This is a hobby project.

## Features

- **Search plants illustrations (`/plants`)**: Users can access a list of available plants illustrations;

- **IIIF Image Retrieval (`/iiif`)**: Utilizes IIIF standards to serve images of plants, enabling rich interaction such as zooming and panning.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Git
- Make
- Docker and Docker Compose

### Installation

1. Clone the repository to your local machine;
2. Navigate to the cloned directory.

### Configuration with Makefile

This project utilizes a Makefile for various operations:

- `make up`: Start the application and database using Docker and Docker-compose;
- `make down`: Stop and remove containers, networks, images, and volumes;
- `make migrations`: Run database migrations to prepare your environment;
- `make ingest`: Ingest example data into the database to start testing the API.

## Contributing

We welcome contributions! If you have suggestions for improvements or bug fixes, please feel free to fork the repository and submit a pull request.

## Acknowledge

The example data available in this repository, comes from the [Old Book Illustrations](https://www.oldbookillustrations.com/) website. Thanks!

## License

`plants` is distributed under the MIT license. See LICENSE for more details.
