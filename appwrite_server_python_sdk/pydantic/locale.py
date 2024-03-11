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


class Locale(BaseModel):
    # User IP address.
    ip: str = Field(alias='ip')

    # Country code in [ISO 3166-1](http://en.wikipedia.org/wiki/ISO_3166-1) two-character format
    country_code: str = Field(alias='countryCode')

    # Country name. This field support localization.
    country: str = Field(alias='country')

    # Continent code. A two character continent code \"AF\" for Africa, \"AN\" for Antarctica, \"AS\" for Asia, \"EU\" for Europe, \"NA\" for North America, \"OC\" for Oceania, and \"SA\" for South America.
    continent_code: str = Field(alias='continentCode')

    # Continent name. This field support localization.
    continent: str = Field(alias='continent')

    # True if country is part of the European Union.
    eu: bool = Field(alias='eu')

    # Currency code in [ISO 4217-1](http://en.wikipedia.org/wiki/ISO_4217) three-character format
    currency: str = Field(alias='currency')
    class Config:
        arbitrary_types_allowed = True
