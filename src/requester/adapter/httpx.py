import typing

import httpx

from src.requester import exceptions


class HttpxKwargs(typing.TypedDict):
    url: str
    params: typing.NotRequired[dict | list | bytes | None]
    content: typing.NotRequired[bytes | bytearray | None]
    data: typing.NotRequired[dict | list | bytes | None]
    files: typing.NotRequired[dict | None]
    json: typing.NotRequired[dict | None]
    headers: typing.NotRequired[dict | None]
    cookies: typing.NotRequired[dict | None]
    auth: typing.NotRequired[tuple | httpx.DigestAuth | None]
    proxies: typing.NotRequired[dict | None]
    timeout: typing.NotRequired[float | tuple]
    follow_redirects: typing.NotRequired[bool]
    verify: typing.NotRequired[bool]
    cert: typing.NotRequired[str | tuple | None]
    trust_env: typing.NotRequired[bool]


class HttpxAdapter:
    def __init__(self, _client: typing.Any | None = None) -> None:
        self._client: httpx.Client = _client or httpx.Client()

    def request[
        T
    ](self, method: str, url: str, default: T | None = None, **kwargs: typing.Unpack[HttpxKwargs]) -> T | typing.Any:
        try:
            result: httpx.Response = self._client.request(method, url, **kwargs)
        except httpx.RequestError as exc:
            if not default:
                raise exceptions.ConnectionError(exc)
            return default
        try:
            result.raise_for_status()
        except httpx.HTTPError as exc:
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
    def get[T](self, *, url: str, default: T, **kwargs: typing.Unpack[HttpxKwargs]) -> T:
        ...

    @typing.overload
    def get[T](self, *, url: str, **kwargs: typing.Unpack[HttpxKwargs]) -> T | typing.Any:
        ...

    def get[T](self, *, url: str, default: T | None = None, **kwargs: typing.Unpack[HttpxKwargs]) -> T | typing.Any:
        return self.request("get", url, default=default, **kwargs)

    @typing.overload
    def post[T](self, *, url: str, default: T, **kwargs: typing.Unpack[HttpxKwargs]) -> T:
        ...

    @typing.overload
    def post[T](self, *, url: str, **kwargs: typing.Unpack[HttpxKwargs]) -> T | typing.Any:
        ...

    def post[T](self, *, url: str, default: T | None = None, **kwargs: typing.Unpack[HttpxKwargs]) -> T | typing.Any:
        return self.request("post", url, default=default, **kwargs)

    @typing.overload
    def put[T](self, *, url: str, default: T, **kwargs: typing.Unpack[HttpxKwargs]) -> T:
        ...

    @typing.overload
    def put[T](self, *, url: str, **kwargs: typing.Unpack[HttpxKwargs]) -> T | typing.Any:
        ...

    def put[T](self, *, url: str, default: T | None = None, **kwargs: typing.Unpack[HttpxKwargs]) -> T | typing.Any:
        return self.request("put", url, default=default, **kwargs)

    @typing.overload
    def patch[T](self, *, url: str, default: T, **kwargs: typing.Unpack[HttpxKwargs]) -> T:
        ...

    @typing.overload
    def patch[T](self, *, url: str, **kwargs: typing.Unpack[HttpxKwargs]) -> T | typing.Any:
        ...

    def patch[T](self, *, url: str, default: T | None = None, **kwargs: typing.Unpack[HttpxKwargs]) -> T | typing.Any:
        return self.request("patch", url, default=default, **kwargs)

    def delete(self, *, url: str, **kwargs: typing.Unpack[HttpxKwargs]) -> typing.Literal[204]:
        return self.request("delete", url, default=204, **kwargs)
