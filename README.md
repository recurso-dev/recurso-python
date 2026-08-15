# recurso — Python SDK

Official Python SDK for the [Recurso](https://github.com/recurso-dev/recurso)
billing API — a typed client generated from Recurso's OpenAPI 3.1 spec, covering
40+ resource groups: plans, customers, the full subscription lifecycle
(pause/resume/cancel, add-ons, plan-change preview, commitments), invoices,
usage-based billing (metering, prepaid wallets, usage alerts), payments, coupons,
quotes, entitlements, credit notes, disputes, dunning, tax & e-invoicing, the
ledger, analytics, webhooks, and more.

Monetary amounts are integers in the currency's smallest unit (cents/paise).
Requires **Python 3.11+**.

## Install

Not yet published on PyPI — install from a checkout:

```bash
git clone https://github.com/recurso-dev/recurso-python.git
pip install ./recurso-python
```

## Usage

Authenticate with your Recurso API key (used as a bearer token), then call an
operation. Each resource group lives under `recurso.api.<group>`, and request
bodies are typed dataclasses under `recurso.models`:

```python
from recurso import AuthenticatedClient
from recurso.api.plans import create_plan
from recurso.api.customers import create_customer
from recurso.api.subscriptions import create_subscription
from recurso.models import (
    CreatePlanRequest,
    CreatePlanRequestIntervalUnit,
    CreateCustomerRequest,
    CreateSubscriptionRequest,
)

client = AuthenticatedClient(
    base_url="https://api.recurso.dev",  # your Recurso API (cloud or self-hosted)
    token="sk_live_your_api_key",
)

with client as client:
    plan = create_plan.sync(client=client, body=CreatePlanRequest(
        name="Pro Plan",
        code="PRO-USD",
        amount=2900,                       # minor units → $29.00
        currency="USD",
        interval_unit=CreatePlanRequestIntervalUnit.MONTH,
        interval_count=1,
    ))

    customer = create_customer.sync(client=client, body=CreateCustomerRequest(
        name="Jane User",
        email="jane@example.com",
        country="US",
    ))

    subscription = create_subscription.sync(client=client, body=CreateSubscriptionRequest(
        customer_id=customer.id,
        plan_id=plan.id,
    ))
```

Every operation exposes `.sync()` / `.sync_detailed()` and async
`.asyncio()` / `.asyncio_detailed()`. The `*_detailed` variants return a
`Response` carrying the `status_code`, `headers`, and parsed body:

```python
from recurso.api.subscriptions import list_subscriptions
from recurso.types import Response

resp: Response = list_subscriptions.sync_detailed(client=client)
print(resp.status_code, resp.parsed)
```

### Async

```python
from recurso.api.subscriptions import list_subscriptions

async with client as client:
    subs = await list_subscriptions.asyncio(client=client)
```

### Unauthenticated client

For endpoints that don't require auth, use `Client` instead of
`AuthenticatedClient`:

```python
from recurso import Client
client = Client(base_url="https://api.recurso.dev")
```

## Typed models

Request and response types are generated dataclasses under `recurso.models`, so
editors autocomplete fields and enums (e.g. `CreatePlanRequestIntervalUnit`).
Import them to annotate your own code:

```python
from recurso.models import Subscription, Customer, Invoice
```

TLS verification is on by default; pass `verify_ssl="/path/to/bundle.pem"` (or
`verify_ssl=False`, a security risk) to `AuthenticatedClient` for custom certs.

Full method reference and guides: **[docs.recurso.dev](https://docs.recurso.dev)**.

## License

MIT
