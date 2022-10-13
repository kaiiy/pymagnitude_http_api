# pymagnitude_http_api

## Requirements

- task
- docker

## Setup

```sh 
$ task setup 
```

## Usage

```sh
$ task run
$ curl -X POST -H "Content-Type: application/json" \
    -d '{"base": ["好き", "だ", "食べ物", "は", "林檎"], "targets": [{"id": 1, "sent": ["りんご"]}]}' localhost:45200/targets
``` 
