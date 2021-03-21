from whmcs.response_objects import *

action_to_object_map = {
    'AcceptOrder': SuccessOrError,
    'AddOrder': AddOrder,
    'CancelOrder': SuccessOrError,
    'DeleteOrder': SuccessOrError,
    'FraudOrder': SuccessOrError,
    'GetOrders': GetOrders,
    'GetOrderStatuses': GetOrderStatuses,
    'GetProducts': GetProducts,
    'GetPromotions': GetPromotions,
    'OrderFraudCheck': OrderFraudCheck,
    'PendingOrder': SuccessOrError
}