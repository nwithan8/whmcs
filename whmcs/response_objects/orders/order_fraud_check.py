# generated by datamodel-codegen:
#   filename:  model.json
#   timestamp: 2021-03-19T23:02:04+00:00

from __future__ import annotations

from pydantic import BaseModel


class Model(BaseModel):
    result: str
    module: str
    status: str
