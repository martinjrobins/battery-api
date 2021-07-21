"""
    Battery Data API

    A standard API for accessing battery experiment datasets and metadata  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: martin.robinson@cs.ox.ac.uk
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.users_api import UsersApi  # noqa: E501


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_cell(self):
        """Test case for get_cell

        get information on a single cell  # noqa: E501
        """
        pass

    def test_get_cells(self):
        """Test case for get_cells

        gets information on all cells  # noqa: E501
        """
        pass

    def test_get_column(self):
        """Test case for get_column

        gets a single column of data from a dataset  # noqa: E501
        """
        pass

    def test_get_dataset(self):
        """Test case for get_dataset

        get information on a single dataset  # noqa: E501
        """
        pass

    def test_get_datasets(self):
        """Test case for get_datasets

        gets information on all datasets  # noqa: E501
        """
        pass

    def test_get_equipment(self):
        """Test case for get_equipment

        get information on a single item of test equipment  # noqa: E501
        """
        pass

    def test_get_equipments(self):
        """Test case for get_equipments

        gets information on all recorded test equipment  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        get information on a single user  # noqa: E501
        """
        pass

    def test_get_users(self):
        """Test case for get_users

        gets information on all users  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
