<div align="center">
<img src="https://bigir.ir/cdn/fc24da3b8fc24460ae0e3090b/grpc.png" alt="GRPCSON Logo" width="100" />
<h1>GRPCSON</h1>
<p>
GRPSCON converts GRPC to JSON.<br/>
<a href="https://github.com/siyanew/grpcson"><strong>Explore the docs »</strong></a>
</p>
</div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

## Getting Started

Unlike GRPC Gateway GRPCSON is easy to install to test for local development.
Follow these simple steps to setup a local copy.

### Prerequisites

You will need [docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/) on your machine.<br>
Your GRPC Server must support reflection, to see how to set up reflection please visit [this](https://github.com/grpc/grpc/blob/master/doc/server-reflection.md).
  
### Installation

GRPCSON needs the port and host to be configured in the `docker-compose.yml` file, after that run:
```
docker-compose up -d
```

## Usage
Open the following address in your browser and check the services and methods. Then send your request as a post to the url with a json body and receive a json response.
```
http://localhost:5912
```

## TODO

- [ ] Add Option for TLS connection
- [ ] Add Option to accept protos

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the GPL-3 License. See `LICENSE` for more information.

## Acknowledgements

* [GRPCURL](https://github.com/fullstorydev/grpcurl)
* [GRPCSON Logo by Freepik](https://freepik.com)


[contributors-shield]: https://img.shields.io/github/contributors/siyanew/Siarobo.svg?style=flat
[contributors-url]: https://github.com/siyanew/grpcson/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/siyanew/grpcson.svg?style=flat
[forks-url]: https://github.com/siyanew/grpcson/network/members
[stars-shield]: https://img.shields.io/github/stars/siyanew/grpcson.svg?style=flat
[stars-url]: https://github.com/siyanew/grpcson/stargazers
[issues-shield]: https://img.shields.io/github/issues/siyanew/grpcson.svg?style=flat
[issues-url]: https://github.com/siyanew/grpcson/issues
[license-shield]: https://img.shields.io/github/license/siyanew/grpcson.svg?style=flat
[license-url]: https://github.com/siyanew/grpcson/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png
