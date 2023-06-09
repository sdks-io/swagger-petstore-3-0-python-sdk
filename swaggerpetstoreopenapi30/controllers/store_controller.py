# -*- coding: utf-8 -*-

"""
swaggerpetstoreopenapi30

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from swaggerpetstoreopenapi30.api_helper import APIHelper
from swaggerpetstoreopenapi30.configuration import Server
from swaggerpetstoreopenapi30.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from swaggerpetstoreopenapi30.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or
from swaggerpetstoreopenapi30.models.order import Order
from swaggerpetstoreopenapi30.exceptions.api_exception import APIException


class StoreController(BaseController):

    """A Controller to access Endpoints in the swaggerpetstoreopenapi30 API."""
    def __init__(self, config):
        super(StoreController, self).__init__(config)

    def get_inventory(self):
        """Does a GET request to /store/inventory.

        Returns a map of status codes to quantities

        Returns:
            dict: Response from the API. successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/store/inventory')
            .http_method(HttpMethodEnum.GET)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
        ).execute()

    def place_order(self,
                    id=None,
                    pet_id=None,
                    quantity=None,
                    ship_date=None,
                    order_status='approved',
                    complete=None):
        """Does a POST request to /store/order.

        Place a new order in the store

        Args:
            id (long|int, optional): TODO: type description here.
            pet_id (long|int, optional): TODO: type description here.
            quantity (int, optional): TODO: type description here.
            ship_date (datetime, optional): TODO: type description here.
            order_status (OrderStatusEnum, optional): Order Status
            complete (bool, optional): TODO: type description here.

        Returns:
            Order: Response from the API. successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/store/order')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('id')
                        .value(id))
            .form_param(Parameter()
                        .key('petId')
                        .value(pet_id))
            .form_param(Parameter()
                        .key('quantity')
                        .value(quantity))
            .form_param(Parameter()
                        .key('shipDate')
                        .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, ship_date)))
            .form_param(Parameter()
                        .key('orderStatus')
                        .value(order_status))
            .form_param(Parameter()
                        .key('complete')
                        .value(complete))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Order.from_dictionary)
            .local_error('405', 'Invalid input', APIException)
        ).execute()

    def get_order_by_id(self,
                        order_id):
        """Does a GET request to /store/order/{orderId}.

        For valid response try integer IDs with value <= 5 or > 10. Other
        values will generate exceptions.

        Args:
            order_id (long|int): ID of order that needs to be fetched

        Returns:
            Order: Response from the API. successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/store/order/{orderId}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('orderId')
                            .value(order_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Order.from_dictionary)
            .local_error('400', 'Invalid ID supplied', APIException)
            .local_error('404', 'Order not found', APIException)
        ).execute()

    def delete_order(self,
                     order_id):
        """Does a DELETE request to /store/order/{orderId}.

        For valid response try integer IDs with value < 1000. Anything above
        1000 or nonintegers will generate API errors

        Args:
            order_id (long|int): ID of the order that needs to be deleted

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/store/order/{orderId}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('orderId')
                            .value(order_id)
                            .should_encode(True))
            .auth(Single('global'))
        ).execute()
