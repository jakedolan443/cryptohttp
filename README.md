# CryptoHTTP
A minimalist, self-hosted web app for viewing cryptocurrency data.

![](https://raw.githubusercontent.com/jakedolan443/cryptohttp/main/screenshots/screen.png)
![](https://raw.githubusercontent.com/jakedolan443/cryptohttp/main/screenshots/screen2.png)
CryptoHTTP is a Flask webserver which uses the `cryptowatch-sdk` module with Kraken's API to deliver a simplistic, minimalist dashboard showing current market data.

Kraken provides a free API, so no API-key is required, howvever, for frequent API calls (more than once an hour) you should setup a free API account. [Instructions](https://github.com/cryptowatch/cw-sdk-python#setup-your-credential-file)

## Setup

### Manual

```
git clone https://github.com/jakedolan443/cryptohttp
cd cryptohttp
./setup.sh
```
To run cryptohttp:
```
./cryptohttp
```
Type `./cryptohttp --help` for more options.

The default interface is 0.0.0.0

The default port is 8080.

The default refresh rate is 3600secs.

The file `config/coins.conf` contains a line by line list of coins, in order, displayed on the webserver, e.g.
```
BTC
ETH
XMR
```

### Docker

Prebuilt image:

Docker run
```
docker run --name=cryptohttp -d -v "$pwd":/app/config -p 8080:8080 --restart unless-stopped ackr8/cryptohttp
```
Docker compose
```
version: '3.3'
services:
    cryptohttp:
        container_name: cryptohttp
        volumes:
            - '$pwd:/app/config'
        ports:
            - '8080:8080'
        restart: unless-stopped
        image: ackr8/cryptohttp
```

Manually building the image:

```
git clone https://github.com/jakedolan443/cryptohttp
cd cryptohttp
docker build -t cryptohttp .
docker-compose up -d
```

Interface, port, and refresh rate may be changed with environment variables within `docker-compose.yaml`.

## Contribute
This project is fully open to contribution! The current to-do list:

- Cache API data 
- CSS Themes
- Add support for multiple fiat currency conversions (e.g. EUR, GBP)

If you are looking to contribute or have any feature ideas, contact me at jakedolan443@protonmail.com.

## Attribution

Cryptowatch SDK from https://github.com/cryptowatch/cw-sdk-python

API from https://www.kraken.com

Hightables library from https://github.com/dtao/HighTables

Icons obtained from https://github.com/spothq/cryptocurrency-icons/ under Creative Commons License 

## Donate

XMR
```
85wYZS2eFM3FqEU3yMeuMmh4PXC7vgC2AZS27ow6bU7QhYQYEbQBzd4WbcSLgs43yeZ1uAHRkGcn1Q6jRyNHcL881JoAyVG
