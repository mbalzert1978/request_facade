# Requester a request facade

facade test for the catapi as a facade

usage:
``` python
    result = requester.TheCatApi(settings.api_key)
    print(result.get(params={"limit": 10}))
```

you can use it with or without an API key.
- without results are limited to 10

store an api key in a .env file in the main directory

``` .env
API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxx
```
