class APIError(Exception):
    """
    Generic API error
    """

class MissingPermission(APIError):
    """
    Missing permission when calling the API.
    """