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


class RequiredCurrency(TypedDict):
    # Currency symbol.
    symbol: str

    # Currency name.
    name: str

    # Currency native symbol.
    symbolNative: str

    # Number of decimal digits.
    decimalDigits: int

    # Currency digit rounding.
    rounding: typing.Union[int, float]

    # Currency code in [ISO 4217-1](http://en.wikipedia.org/wiki/ISO_4217) three-character format.
    code: str

    # Currency plural name
    namePlural: str

class OptionalCurrency(TypedDict, total=False):
    pass

class Currency(RequiredCurrency, OptionalCurrency):
    pass
