"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import nutrition as shared_nutrition
from ..shared import user as shared_user
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclasses.dataclass
class GetNutritionRequest:
    
    start_date: Any = dataclasses.field(metadata={'query_param': { 'field_name': 'start_date', 'style': 'form', 'explode': True }})
    r"""start date of data to query for - either ISO8601 date or unix timestamp"""  
    user_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'user_id', 'style': 'form', 'explode': True }})
    r"""user ID to query data for"""  
    end_date: Optional[Any] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'end_date', 'style': 'form', 'explode': True }})
    r"""end date of data to query for - either ISO8601 date or unix timestamp"""  
    to_webhook: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'to_webhook', 'style': 'form', 'explode': True }})
    r"""boolean flag specifying whether to send the data retrieved to the webhook, or in the response"""  
    with_samples: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'with_samples', 'style': 'form', 'explode': True }})
    r"""boolean flag specifying whether to include detailed samples in the returned payload"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetNutrition404ApplicationJSON:
    r"""Returned when a parameter does not exist on Terra's end (e.g. user_id)"""
    
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    r"""a detailed message describing the error"""  
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""indicates that an error happened (value is error)"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetNutrition403ApplicationJSON:
    r"""Returned when credentials (dev ID and API key) are invalid"""
    
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    r"""a detailed message describing the error"""  
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""indicates that an error happened (value is error)"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetNutrition401ApplicationJSON:
    r"""Returned when authorization with a data provider has failed"""
    
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    r"""a detailed message describing the error"""  
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""indicates that an error happened (value is error)"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetNutrition400ApplicationJSON:
    r"""Returned when one or more parameters is malformed - an appropriate error message will be returned"""
    
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    r"""a detailed message describing the error"""  
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""indicates that an error happened (value is error)"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetNutrition200ApplicationJSON1:
    
    data: Optional[list[shared_nutrition.Nutrition]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})  
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})  
    user: Optional[shared_user.User] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user'), 'exclude': lambda f: f is None }})  
    

@dataclasses.dataclass
class GetNutritionResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    get_nutrition_200_application_json_one_of: Optional[Any] = dataclasses.field(default=None)
    r"""Returned upon successful data request"""  
    get_nutrition_400_application_json_object: Optional[GetNutrition400ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when one or more parameters is malformed - an appropriate error message will be returned"""  
    get_nutrition_401_application_json_object: Optional[GetNutrition401ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when authorization with a data provider has failed"""  
    get_nutrition_403_application_json_object: Optional[GetNutrition403ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when credentials (dev ID and API key) are invalid"""  
    get_nutrition_404_application_json_object: Optional[GetNutrition404ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when a parameter does not exist on Terra's end (e.g. user_id)"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    