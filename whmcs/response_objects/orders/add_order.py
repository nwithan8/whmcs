# generated by datamodel-codegen:
#   filename:  model.json
#   timestamp: 2021-03-19T22:52:51+00:00

from __future__ import annotations

from pydantic import BaseModel


class Model(BaseModel):
    result: str
    orderid: str
    serviceids: str
    addonids: str
    domainids: str
    invoiceid: str
