import sys
from botocore.exceptions import (
    BotoCoreError,
    ClientError,
    EndpointConnectionError,
)

from . import get_user_arn


def _main() -> None:
    try:
        print(get_user_arn())
    except EndpointConnectionError as exc:
        # Network / STS endpoint issue
        print(f"Cannot reach AWS STS endpoint: {exc}", file=sys.stderr)
        sys.exit(2)
    except (BotoCoreError, ClientError) as exc:
        # Credential or other AWS-side failure
        print(f"Credential test failed: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    _main()
