# cne_aws_userarn

`cne_aws_userarn` is a tiny helper that confirms your locally-configured AWS credentials work by calling **STS → GetCallerIdentity** and returning the ARN of the current principal.

## Installation

Requires **Python 3.8+** and network connectivity to AWS STS.

```bash
pip install boto3 botocore
```

*Installing `boto3` pulls in the exact `botocore` version it needs; both are listed explicitly so environments that pin direct dependencies can copy-paste this line as-is.*

## Usage

### Library

```python
from cne_aws_userarn import get_user_arn
print(get_user_arn())
```

### CLI

```bash
python -m cne_aws_userarn
# -> arn:aws:iam::<account-id>:user/<username>
```

If STS is unreachable you’ll see an “Cannot reach AWS STS endpoint” message and the
process exits with status 2; credential-related failures exit with status 1.

## Why?

A quick *smoke test* for tooling or CI pipelines that rely on AWS authentication.
No additional policy setup is normally needed—the caller just needs permission to
invoke **sts:GetCallerIdentity**, which IAM users and roles have implicitly.

---

Disclaimer: This code and documentation were generated by AI. Review before using in production.
