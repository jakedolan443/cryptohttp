# CryptoHTTP
A minimalist, self-hosted web app for viewing cryptocurrency data.
[Demo](http://135.181.148.230:38505/)

![enter image description here](https://raw.githubusercontent.com/jakedolan443/cryptohttp/main/screenshots/screenshot3.png)
CryptoHTTP is a Flask webserver which uses the `cryptowatch-sdk` module with Kraken's API to deliver a simplistic, minimalist dashboard showing current market data.

Kraken provides a free API, so no API-key is required. By default, the server sends an API request once an hour. Using an API key will increase your limit. [More info](https://support.kraken.com/hc/en-us/articles/360022839451-Generate-API-keys)

## Setup
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
## To do
I created this small project after becoming frustrated with the lack of available web apps for viewing simple crypto market data. I wanted something minimalist and simple that could run on relatively low resources, which I could self-host. This project is in need of contribution.
- Add support for multiple fiat currencies via an external library
- Create neater setup script
- Add sorting ability to tables
- Add support for more coins

## Attribution

Cryptowatch SDK from https://github.com/cryptowatch/cw-sdk-python

API from https://www.kraken.com

Icons obtained from https://github.com/spothq/cryptocurrency-icons/ under Creative Commons License 

## Donate
XMR
```
85wYZS2eFM3FqEU3yMeuMmh4PXC7vgC2AZS27ow6bU7QhYQYEbQBzd4WbcSLgs43yeZ1uAHRkGcn1Q6jRyNHcL881JoAyVG
