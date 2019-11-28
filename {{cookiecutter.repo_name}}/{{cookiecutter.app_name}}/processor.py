import hashlib
from decimal import Decimal

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.urls import reverse

from getpaid.processor import BaseProcessor


class PaymentProcessor(BaseProcessor):
    display_name = "{{ cookiecutter.broker_name }}"
    accepted_currencies = []  # use ISO codes here, e.g. "EUR", "USD"
    logo_url = None
    slug = "{{ cookiecutter.broker_name|lower() }}"
    method = "GET"
    template_name = None  # used only if method == "POST"

    # you need to define at least these methods:
    def get_redirect_params(self) -> dict:
        """
        Must return a dictionary containing all the data required by
        backend to process the payment in appropriate format.

        Refer to your broker's API documentation for info what keys the API
        expects and what types should the values be in.

        The Payment instance is here: self.payment
        """
        return {}

    def get_redirect_url(self) -> str:
        """
        Returns URL where the user will be redirected to complete the payment.
        This URL should be provided in your broker's documentation.

        The Payment instance is here: self.payment
        """
        return ""
