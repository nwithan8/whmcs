from functools import wraps
from typing import Union


def api_request(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs) -> Union[dict, object]:
        action = func(self)
        return self._web_handler.api_call(action=action, *args, **kwargs)
    return wrapper