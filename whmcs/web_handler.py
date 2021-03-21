import requests

from whmcs.exceptions import MissingPermission, APIError
from whmcs import object_creator

param_translations = {
    'product_id': 'pid',
    'group_id': 'gid',
    'registration_period': 'regperiod',
    'affiliate_id': 'affid',
    'root_password': 'rootpw'
}

def _parse_response_json(response: requests.Response) -> dict:
    if response:
        return response.json()
    return {}

def _check_response(response: requests.Response):
    if not response:
        if response.status_code == 403:
            raise MissingPermission()
        else:
            raise APIError()

def _lookup_param_translation(param):
    return param_translations.get(param, param)

def _replace_param_names_remove_empty(**params):
    new_params = {}
    for key, value in params.items():
        if value is not None:
            new_key = _lookup_param_translation(param=key)
            new_key = new_key.replace('_', '')
            new_params[new_key] = value
    return new_params


class WebHandler:
    def __init__(self, api):
        self._api = api

    def _post(self, payload):
        return requests.post(url=self._api.api_url, data=payload, verify=False)

    def _build_request_body(self, action: str, **params):
        params = _replace_param_names_remove_empty(**params)

        for key, value in list(params.items()):
            if isinstance(value, list):
                for index, item in enumerate(value):
                    params[f'{key}[{index}]'] = item
                del params[key]

        payload = {
            'identifier': self._api.identifier,
            'secret': self._api.secret,
            'action': action,
            'responsetype': 'json'
        }
        payload.update(params)

        return payload

    def api_call(self, action: str, **params):
        data = self._build_request_body(action=action, **params)
        res = self._post(payload=data)
        _check_response(response=res)
        json = _parse_response_json(response=res)
        if self._api._raw:
            return json
        else:
            if json.get('result') != 'success':
                return None
            return object_creator.create_object(action=action, data=json)
