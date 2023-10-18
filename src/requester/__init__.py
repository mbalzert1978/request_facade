import typing
from src.requester.adapter import RequestAdapter as _RequestAdapter
from src.requester.model.cat_api import _Response

__all__ = ["TheCatApi"]


class _Facade(typing.Protocol):
    """Interface for requests."""

    _headers: typing.Dict[str, typing.Any]

    def get[T](self, url: str, default: T | None = None, **kwargs) -> T | typing.Any:
        ...

    def post[T](self, url: str, default: T | None = None, **kwargs) -> T | typing.Any:
        ...

    def put[T](self, url: str, default: T | None = None, **kwargs) -> T | typing.Any:
        ...

    def patch[T](self, url: str, default: T | None = None, **kwargs) -> T | typing.Any:
        ...

    def delete(self, url: str, **kwargs) -> typing.Literal[204]:
        ...


class _BasicRequester:
    def __init__(self) -> None:
        self._client = _RequestAdapter()

    def get[T](self, url: str, default: T | None = None, **kwargs: typing.Any) -> T | typing.Any:
        return self._client.get(url=url, default=default, **kwargs)

    def post[T](self, url: str, default: T | None = None, **kwargs) -> T | typing.Any:
        return self._client.post(url=url, default=default, **kwargs)

    def put[T](self, url: str, default: T | None = None, **kwargs) -> T | typing.Any:
        return self._client.put(url=url, default=default, **kwargs)

    def patch[T](self, url: str, default: T | None = None, **kwargs) -> T | typing.Any:
        return self._client.patch(url=url, default=default, **kwargs)

    def delete(self, url: str, **kwargs) -> typing.Literal[204]:
        return self._client.delete(url=url, **kwargs)


class TheCatApi:
    _headers = {"x-api-key": None}
    _url = "https://api.thecatapi.com/v1/images/search"

    def __init__(self, api_key: str) -> None:
        self._headers["x-api-key"] = api_key
        self._requester = _BasicRequester()

    def get[T](self, default: T | None = None, **kwargs: typing.Any) -> T | _Response:
        return self._requester.get(url=self.url, default=default, **kwargs)

    def post[T](self, url: str, default: T | None = None, **kwargs) -> T | typing.Any:
        raise NotImplementedError()

    def put[T](self, url: str, default: T | None = None, **kwargs) -> T | typing.Any:
        raise NotImplementedError()

    def patch[T](self, url: str, default: T | None = None, **kwargs) -> T | typing.Any:
        raise NotImplementedError()

    def delete(self, url: str, **kwargs) -> typing.Literal[204]:
        raise NotImplementedError()
