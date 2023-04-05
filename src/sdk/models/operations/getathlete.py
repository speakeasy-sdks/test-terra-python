"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclasses.dataclass
class GetAthleteRequest:
    
    user_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'user_id', 'style': 'form', 'explode': True }})
    r"""user ID to query data for"""  
    to_webhook: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'to_webhook', 'style': 'form', 'explode': True }})
    r"""boolean flag specifying whether to send the data retrieved to the webhook, or in the response"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAthlete404ApplicationJSON:
    r"""Returned when a parameter does not exist on Terra's end (e.g. user_id)"""
    
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    r"""a detailed message describing the error"""  
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""indicates that an error happened (value is error)"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAthlete403ApplicationJSON:
    r"""Returned when credentials (dev ID and API key) are invalid"""
    
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    r"""a detailed message describing the error"""  
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""indicates that an error happened (value is error)"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAthlete401ApplicationJSON:
    r"""Returned when authorization with a data provider has failed"""
    
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    r"""a detailed message describing the error"""  
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""indicates that an error happened (value is error)"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAthlete400ApplicationJSON:
    r"""Returned when one or more parameters is malformed - an appropriate error message will be returned"""
    
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    r"""a detailed message describing the error"""  
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""indicates that an error happened (value is error)"""  
    

@dataclasses.dataclass
class GetAthleteResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    get_athlete_200_application_json_one_of: Optional[Any] = dataclasses.field(default=None)
    r"""Returned upon successful data request"""  
    get_athlete_400_application_json_object: Optional[GetAthlete400ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when one or more parameters is malformed - an appropriate error message will be returned"""  
    get_athlete_401_application_json_object: Optional[GetAthlete401ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when authorization with a data provider has failed"""  
    get_athlete_403_application_json_object: Optional[GetAthlete403ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when credentials (dev ID and API key) are invalid"""  
    get_athlete_404_application_json_object: Optional[GetAthlete404ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when a parameter does not exist on Terra's end (e.g. user_id)"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    