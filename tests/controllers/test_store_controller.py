# -*- coding: utf-8 -*-

"""
swaggerpetstoreopenapi30

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from apimatic_core.utilities.comparison_helper import ComparisonHelper
from swaggerpetstoreopenapi30.api_helper import APIHelper


class StoreControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(StoreControllerTests, cls).setUpClass()
        cls.controller = cls.client.store
        cls.response_catcher = cls.controller.http_call_back

    # Returns a map of status codes to quantities
    def test_get_inventory(self):

        # Perform the API call through the SDK function
        result = self.controller.get_inventory()

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Place a new order in the store
    def test_place_order(self):
        # Parameters for the API call
        id = 10
        pet_id = 198772
        quantity = 7
        ship_date = APIHelper.RFC3339DateTime.from_value('2023-05-31T00:00:00Z').datetime
        order_status = 'approved'
        complete = True

        # Perform the API call through the SDK function
        result = self.controller.place_order(id, pet_id, quantity, ship_date, order_status, complete)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


