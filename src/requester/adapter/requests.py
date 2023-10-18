import typing

import requests

from src.requester import exceptions


class RequestsKwargs(typing.TypedDict):
    method: str
    url: str
    params: typing.NotRequired[dict | list | bytes | None]
    data: typing.NotRequired[dict | list | bytes | None]
    json: typing.NotRequired[dict | None]
    headers: typing.NotRequired[dict | None]
    cookies: typing.NotRequired[dict | None]
    files: typing.NotRequired[dict | None]
    auth: typing.NotRequired[tuple | None]
    timeout: typing.NotRequired[float | tuple]
    allow_redirects: typing.NotRequired[bool]
    proxies: typing.NotRequired[dict | None]
    verify: typing.NotRequired[bool]
    stream: typing.NotRequired[bool]
    cert: typing.NotRequired[str | tuple | None]


class RequestAdapter:
    def __init__(self, _client: typing.Any | None = None) -> None:
        self._client = _client or requests

    def request[
        T
    ](self, method: str, url: str, default: T | None = None, **kwargs: typing.Unpack[RequestsKwargs]) -> T | typing.Any:
        try:
            result: requests.Response = self._client.request(method, url, **kwargs)
        except requests.RequestException as exc:
            if not default:
                raise exceptions.ConnectionError(exc)
            return default
        try:
            result.raise_for_status()
        except requests.HTTPError as exc:
            if not default:
                raise exceptions.HTTPError(exc)
            return default
        try:
            return result.json()
        except ValueError as exc:
            if not default:
                raise exceptions.NoValueError(exc)
            return default

    @typing.overload
    def get[T](self, *, url: str, default: T, **kwargs: typing.Unpack[RequestsKwargs]) -> T:
        ...

    @typing.overload
    def get[T](self, *, url: str, **kwargs: typing.Unpack[RequestsKwargs]) -> T | typing.Any:
        ...

    def get[T](self, *, url: str, default: T | None = None, **kwargs: typing.Unpack[RequestsKwargs]) -> T | typing.Any:
        return self.request("get", url, default=default, **kwargs)

    @typing.overload
    def post[T](self, *, url: str, default: T, **kwargs: typing.Unpack[RequestsKwargs]) -> T:
        ...

    @typing.overload
    def post[T](self, *, url: str, **kwargs: typing.Unpack[RequestsKwargs]) -> T | typing.Any:
        ...

    def post[T](self, *, url: str, default: T | None = None, **kwargs: typing.Unpack[RequestsKwargs]) -> T | typing.Any:
        return self.request("post", url, default=default, **kwargs)

    @typing.overload
    def put[T](self, *, url: str, default: T, **kwargs: typing.Unpack[RequestsKwargs]) -> T:
        ...

    @typing.overload
    def put[T](self, *, url: str, **kwargs: typing.Unpack[RequestsKwargs]) -> T | typing.Any:
        ...

    def put[T](self, *, url: str, default: T | None = None, **kwargs: typing.Unpack[RequestsKwargs]) -> T | typing.Any:
        return self.request("put", url, default=default, **kwargs)

    @typing.overload
    def patch[T](self, *, url: str, default: T, **kwargs: typing.Unpack[RequestsKwargs]) -> T:
        ...

    @typing.overload
    def patch[T](self, *, url: str, **kwargs: typing.Unpack[RequestsKwargs]) -> T | typing.Any:
        ...

    def patch[
        T
    ](self, *, url: str, default: T | None = None, **kwargs: typing.Unpack[RequestsKwargs]) -> T | typing.Any:
        return self.request("patch", url, default=default, **kwargs)

    def delete(self, *, url: str, **kwargs: typing.Unpack[RequestsKwargs]) -> typing.Literal[204]:
        return self.request("delete", url, default=204, **kwargs)
