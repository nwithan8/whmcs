from whmcs.response_objects.base import BaseObject


class SuccessOrError(BaseObject):
    def __init__(self, data):
        super().__init__(data)
        self._success = data.get('result')

    def __bool__(self):
        return self._success == 'success'

    def __str__(self):
        return self._success