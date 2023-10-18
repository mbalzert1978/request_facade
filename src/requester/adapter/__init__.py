"""Interface for requests."""

import typing
from src.requester.adapter.requests import RequestAdapter
from src.requester.adapter.httpx import HttpxAdapter

__all__ = ["RequestAdapter", "HttpxAdapter"]


class Adapter[T, **P](typing.Protocol):
    """Interface for requests."""

    _client: T

    def get(self, url: str, *args: P.args, **kwargs: P.kwargs):
        ...

    def post(self, url: str, *args: P.args, **kwargs: P.kwargs):
        ...

    def put(self, url: str, *args: P.args, **kwargs: P.kwargs):
        ...

    def patch(self, url: str, *args: P.args, **kwargs: P.kwargs):
        ...

    def delete(self, url: str, *args: P.args, **kwargs: P.kwargs):
        ...
