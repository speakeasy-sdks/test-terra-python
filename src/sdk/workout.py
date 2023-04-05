"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from sdk.models import operations
from typing import Any, Optional

class Workout:
    r"""Workout data"""
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    def delete(self, request: operations.DeletePlannedWorkoutRequest) -> operations.DeletePlannedWorkoutResponse:
        r"""Delete workout plans from account
        Used to delete workout plans the user has registered on their account. This can be stregnth workouts (sets, reps, weight lifted) or cardio workouts (warmup, intervals of different intensities, cooldown etc)
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/plannedWorkout'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        query_params = utils.get_query_params(operations.DeletePlannedWorkoutRequest, request)
        
        client = self._security_client
        
        http_res = client.request('DELETE', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeletePlannedWorkoutResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeletePlannedWorkout200ApplicationJSON])
                res.delete_planned_workout_200_application_json_object = out
        elif http_res.status_code == 207:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeletePlannedWorkout207ApplicationJSON])
                res.delete_planned_workout_207_application_json_object = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeletePlannedWorkout400ApplicationJSON])
                res.delete_planned_workout_400_application_json_object = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeletePlannedWorkout401ApplicationJSON])
                res.delete_planned_workout_401_application_json_object = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeletePlannedWorkout403ApplicationJSON])
                res.delete_planned_workout_403_application_json_object = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeletePlannedWorkout404ApplicationJSON])
                res.delete_planned_workout_404_application_json_object = out

        return res

    def get(self, request: operations.GetPlannedWorkoutRequest) -> operations.GetPlannedWorkoutResponse:
        r"""Get workout plans from account
        Used to get workout plans the user has registered on their account. This can be stregnth workouts (sets, reps, weight lifted) or cardio workouts (warmup, intervals of different intensities, cooldown etc)
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/plannedWorkout'
        
        query_params = utils.get_query_params(operations.GetPlannedWorkoutRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetPlannedWorkoutResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.get_planned_workout_200_application_json_one_of = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetPlannedWorkout400ApplicationJSON])
                res.get_planned_workout_400_application_json_object = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetPlannedWorkout401ApplicationJSON])
                res.get_planned_workout_401_application_json_object = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetPlannedWorkout403ApplicationJSON])
                res.get_planned_workout_403_application_json_object = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetPlannedWorkout404ApplicationJSON])
                res.get_planned_workout_404_application_json_object = out

        return res

    