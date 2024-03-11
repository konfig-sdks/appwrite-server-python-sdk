# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel


class Currency(BaseModel):
    # Currency symbol.
    symbol: str = Field(alias='symbol')

    # Currency name.
    name: str = Field(alias='name')

    # Currency native symbol.
    symbol_native: str = Field(alias='symbolNative')

    # Number of decimal digits.
    decimal_digits: int = Field(alias='decimalDigits')

    # Currency digit rounding.
    rounding: typing.Union[int, float] = Field(alias='rounding')

    # Currency code in [ISO 4217-1](http://en.wikipedia.org/wiki/ISO_4217) three-character format.
    code: str = Field(alias='code')

    # Currency plural name
    name_plural: str = Field(alias='namePlural')
    class Config:
        arbitrary_types_allowed = True
