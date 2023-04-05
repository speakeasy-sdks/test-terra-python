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

if res.get_activity_200_application_json_one_of is not None:
    # handle response
```
<!-- End SDK Example Usage -->