from typing import Optional

from pydantic import BaseModel


class RequestCalcModel(BaseModel):
    num1: int
    num2: Optional[int] = None
