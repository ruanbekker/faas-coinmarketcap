# faas-coinmarketcap
I'm getting started with FaaS (Functions as a Service) and decided to make a function for Getting info from CoinMarketCap API

## about FaaS:

Functions as a Service (Serverless Framework for Docker)

- https://github.com/alexellis/faas/
- https://blog.alexellis.io/functions-as-a-service/

## usage:

The function takes the data value that is passed via the POST request as standard input and uses it as the market that you are querying and makes a GET request on CoinMarketCap's API to retrieve the information of the market as passed.

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
