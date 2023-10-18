import src.requester as requester
from src.requester.core.config import settings


def main() -> None:
    result = requester.TheCatApi(settings.api_key)
    print(result.get(params={"limit": 10}))


if __name__ == "__main__":
    main()
