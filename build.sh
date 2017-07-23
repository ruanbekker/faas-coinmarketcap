#!/bin/sh

docker build -t rbekker87/faas_coinmarketcap .
docker tag rbekker87/faas_coinmarketcap rbekker87/faas_coinmarketcap
docker push rbekker87/faas_coinmarketcap
