# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.cell import Cell  # noqa: E501
from swagger_server.models.dataset import Dataset  # noqa: E501
from swagger_server.models.equipment import Equipment  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUsersController(BaseTestCase):
    """UsersController integration test stubs"""

    def test_get_cell(self):
        """Test case for get_cell

        get information on a single cell
        """
        response = self.client.open(
            '/martinjrobins/battery-api/1.0.0/cell/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_cells(self):
        """Test case for get_cells

        gets information on all cells
        """
        response = self.client.open(
            '/martinjrobins/battery-api/1.0.0/cell',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_column(self):
        """Test case for get_column

        gets a single column of data from a dataset
        """
        query_string = [('precision', 'single')]
        response = self.client.open(
            '/martinjrobins/battery-api/1.0.0/dataset/{id}/{column_id}'.format(id=56, column_id=56),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_dataset(self):
        """Test case for get_dataset

        get information on a single dataset
        """
        response = self.client.open(
            '/martinjrobins/battery-api/1.0.0/dataset/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_datasets(self):
        """Test case for get_datasets

        gets information on all datasets
        """
        response = self.client.open(
            '/martinjrobins/battery-api/1.0.0/dataset',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_equipment(self):
        """Test case for get_equipment

        get information on a single item of test equipment
        """
        response = self.client.open(
            '/martinjrobins/battery-api/1.0.0/equipment/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_equipments(self):
        """Test case for get_equipments

        gets information on all recorded test equipment
        """
        response = self.client.open(
            '/martinjrobins/battery-api/1.0.0/equipment',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user(self):
        """Test case for get_user

        get information on a single user
        """
        response = self.client.open(
            '/martinjrobins/battery-api/1.0.0/user/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_users(self):
        """Test case for get_users

        gets information on all users
        """
        response = self.client.open(
            '/martinjrobins/battery-api/1.0.0/user',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
