from whmcs.action_map import action_to_object_map

def create_object(action: str, data: dict):
    object_class = action_to_object_map.get(action, None)
    if object_class:
        return object_class(data=data)
    return None