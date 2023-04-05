# Terra

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/test-terra-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
        dev_id="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetActivityRequest(
    end_date="2021-07-27",
    start_date="2021-04-14",
    to_webhook=False,
    user_id="corrupti",
    with_samples=False,
)
    
res = s.activity.get(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### activity

* `get` - Get activity data for a user
* `send_provider` - Post activity data to a provider

### athlete

* `get` - Get athlete data

### body

* `delete` - Delete body data from account
* `get` - Get body data
* `send_provider` - Send body data to a provider

### daily

* `get` - Get daily data from account

### integrations

* `list` - Get list of available integrations

### menstruation

* `get` - Get menstruation data from account

### nutrition

* `delete` - Delete nutrition data from account
* `get` - Get nutrition data from account
* `send_provider` - Send nutrition data to data provider

### sleep

* `get` - Get sleep data from account

### user

* `authenticate` - Authenticate a user
* `get` - Query for user information
* `list` - Query for user information for multiple Terra User IDs

### workout

* `delete` - Delete workout plans from account
* `get` - Get workout plans from account
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
