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


class HealthCertificate(BaseModel):
    # Certificate name
    name: str = Field(alias='name')

    # Subject SN
    subject_s_n: str = Field(alias='subjectSN')

    # Issuer organisation
    issuer_organisation: str = Field(alias='issuerOrganisation')

    # Valid from
    valid_from: str = Field(alias='validFrom')

    # Valid to
    valid_to: str = Field(alias='validTo')

    # Signature type SN
    signature_type_s_n: str = Field(alias='signatureTypeSN')
    class Config:
        arbitrary_types_allowed = True
