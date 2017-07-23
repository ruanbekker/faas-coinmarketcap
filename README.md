# faas-coinmarketcap
I'm getting started with FaaS (Functions as a Service) and decided to make a function for Getting info from CoinMarketCap API

## about FaaS:

Functions as a Service (Serverless Framework for Docker)

- https://github.com/alexellis/faas/
- https://blog.alexellis.io/functions-as-a-service/

## usage:

The function takes the data value that is passed via the POST request as standard input and uses it as the `market_name` that you are querying and makes a GET request on CoinMarketCap's API to retrieve the information of the market as passed.

Getting the [Image](https://hub.docker.com/r/rbekker87/faas_coinmarketcap/)  and Running the Container:

```
$ docker pull rbekker87/faas_coinmarketcap
$ docker run -itd --name faas_coinmarketcap --publish 8080:8080 rbekker87/faas_coinmarketcap
```

Passing `bitcoin` as the `market_name` value:

```
$ curl -XPOST http://localhost:8080/ -d "bitcoin"
{
    "market_cap_usd": "45292876132.0",
    "price_usd": "2750.81",
    "last_updated": "1500839659",
    "name": "Bitcoin",
    "24h_volume_usd": "1116920000.0",
    "percent_change_7d": "42.89",
    "symbol": "BTC",
    "rank": "1",
    "percent_change_1h": "-0.16",
    "total_supply": "16465287.0",
    "price_btc": "1.0",
    "available_supply": "16465287.0",
    "percent_change_24h": "-1.32",
    "id": "bitcoin"
}
```

When passing a `market_name` which does not exist:

```
$ curl -XPOST http://localhost:8080/ -d "newcoin"
Market Name: newcoin does not exist
```
