from typing import List

from whmcs.decorators import api_request
from whmcs.web_handler import WebHandler


def _create_whmcs_url(url: str):
    if url.endswith("includes/api.php"):
        return url
    return f"{url}/includes/api.php"


class API:
    def __init__(self, whmcs_url: str, identifier: str, secret: str, return_raw_json: bool = False):
        self.api_url = _create_whmcs_url(url=whmcs_url)
        self.identifier = identifier
        self.secret = secret
        self._web_handler = WebHandler(api=self)
        self._raw = return_raw_json

    # Orders

    @api_request
    def accept_order(self,
                     order_id: int,
                     server_id: int = None,
                     service_username: str = None,
                     service_password: str = None,
                     registrar: str = None,
                     send_registrar: bool = None,
                     auto_setup: bool = None,
                     send_email: bool = None):
        return 'AcceptOrder'

    @api_request
    def add_order(self,
                  client_id: int,
                  payment_method: str,
                  product_id: List[int] = None,
                  domain: List[str] = None,
                  billing_cycle: List[str] = None,
                  domain_type: List[str] = None,
                  registration_period: List[int] = None,
                  idn_language: List[str] = None,
                  epp_code: List[str] = None,
                  name_server_1: str = None,
                  name_server_2: str = None,
                  name_server_3: str = None,
                  name_server_4: str = None,
                  name_server_5: str = None,
                  custom_fields: List[str] = None,
                  config_options: List[str] = None,
                  price_override: List[float] = None,
                  promo_code: str = None,
                  promo_override: bool = None,
                  affiliate_id: int = None,
                  no_invoice: bool = None,
                  no_invoice_email: bool = None,
                  no_email: bool = None,
                  addons: List[str] = None,
                  hostname: List[str] = None,
                  ns1_prefix: List[str] = None,
                  ns2_prefix: List[str] = None,
                  root_password: List[str] = None,
                  contact_id: int = None,
                  dns_management: List[bool] = None,
                  domain_fields: List[str] = None,
                  email_forwarding: List[bool] = None,
                  id_protection: List[bool] = None,
                  domain_price_override: List[float] = None,
                  domain_renew_override: List[float] = None,
                  domain_renewals: dict = None,
                  client_ip: str = None,
                  addon_id: int = None,
                  service_id: int = None,
                  addon_ids: List[int] = None,
                  service_ids: List[int] = None):
        return 'AddOrder'

    @api_request
    def cancel_order(self,
                     order_id: int,
                     cancel_sub: bool = None,
                     no_email: bool = None):
        return 'CancelOrder'

    @api_request
    def delete_order(self,
                     order_id: int):
        return 'DeleteOrder'

    @api_request
    def mark_order_as_fradulent(self,
                                order_id: int,
                                cancel_sub: bool = None):
        return 'FraudOrder'

    @api_request
    def get_orders(self,
                   limit_start: int = 0,
                   limit_num: int = 25,
                   id: int = None,
                   user_id: int = None,
                   status: str = None):
        return 'GetOrders'

    @api_request
    @property
    def order_statuses(self):
        return 'GetOrderStatuses'

    @api_request
    def check_order_fraud(self,
                          order_id: int,
                          ip_address: str = None):
        return 'OrderFraudCheck'

    @api_request
    def set_order_to_pending(self,
                             order_id: int):
        return 'PendingOrder'

    # Products

    @api_request
    def get_products(self,
                     product_id: str = None,
                     group_id: int = None,
                     module: str = None):
        return 'GetProducts'

    # Promotions

    @api_request
    def get_promotions(self,
                       code: str = None):
        return 'GetPromotions'
