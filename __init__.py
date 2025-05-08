from __future__ import annotations

import boto3

__all__ = ["get_user_arn"]


def get_user_arn() -> str:
    return boto3.client("sts").get_caller_identity()["Arn"]
