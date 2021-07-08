# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Cell(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, name: str=None, manufacturer: str=None, form_factor: str=None, datasheet: str=None, anode_chemistry: str=None, cathode_chemistry: str=None, nominal_capacity: float=None, nominal_cell_weight: float=None):  # noqa: E501
        """Cell - a model defined in Swagger

        :param id: The id of this Cell.  # noqa: E501
        :type id: int
        :param name: The name of this Cell.  # noqa: E501
        :type name: str
        :param manufacturer: The manufacturer of this Cell.  # noqa: E501
        :type manufacturer: str
        :param form_factor: The form_factor of this Cell.  # noqa: E501
        :type form_factor: str
        :param datasheet: The datasheet of this Cell.  # noqa: E501
        :type datasheet: str
        :param anode_chemistry: The anode_chemistry of this Cell.  # noqa: E501
        :type anode_chemistry: str
        :param cathode_chemistry: The cathode_chemistry of this Cell.  # noqa: E501
        :type cathode_chemistry: str
        :param nominal_capacity: The nominal_capacity of this Cell.  # noqa: E501
        :type nominal_capacity: float
        :param nominal_cell_weight: The nominal_cell_weight of this Cell.  # noqa: E501
        :type nominal_cell_weight: float
        """
        self.swagger_types = {
            'id': int,
            'name': str,
            'manufacturer': str,
            'form_factor': str,
            'datasheet': str,
            'anode_chemistry': str,
            'cathode_chemistry': str,
            'nominal_capacity': float,
            'nominal_cell_weight': float
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'manufacturer': 'manufacturer',
            'form_factor': 'form_factor',
            'datasheet': 'datasheet',
            'anode_chemistry': 'anode_chemistry',
            'cathode_chemistry': 'cathode_chemistry',
            'nominal_capacity': 'nominal_capacity',
            'nominal_cell_weight': 'nominal_cell_weight'
        }
        self._id = id
        self._name = name
        self._manufacturer = manufacturer
        self._form_factor = form_factor
        self._datasheet = datasheet
        self._anode_chemistry = anode_chemistry
        self._cathode_chemistry = cathode_chemistry
        self._nominal_capacity = nominal_capacity
        self._nominal_cell_weight = nominal_cell_weight

    @classmethod
    def from_dict(cls, dikt) -> 'Cell':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Cell of this Cell.  # noqa: E501
        :rtype: Cell
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Cell.


        :return: The id of this Cell.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Cell.


        :param id: The id of this Cell.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Cell.


        :return: The name of this Cell.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Cell.


        :param name: The name of this Cell.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def manufacturer(self) -> str:
        """Gets the manufacturer of this Cell.


        :return: The manufacturer of this Cell.
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer: str):
        """Sets the manufacturer of this Cell.


        :param manufacturer: The manufacturer of this Cell.
        :type manufacturer: str
        """

        self._manufacturer = manufacturer

    @property
    def form_factor(self) -> str:
        """Gets the form_factor of this Cell.


        :return: The form_factor of this Cell.
        :rtype: str
        """
        return self._form_factor

    @form_factor.setter
    def form_factor(self, form_factor: str):
        """Sets the form_factor of this Cell.


        :param form_factor: The form_factor of this Cell.
        :type form_factor: str
        """

        self._form_factor = form_factor

    @property
    def datasheet(self) -> str:
        """Gets the datasheet of this Cell.


        :return: The datasheet of this Cell.
        :rtype: str
        """
        return self._datasheet

    @datasheet.setter
    def datasheet(self, datasheet: str):
        """Sets the datasheet of this Cell.


        :param datasheet: The datasheet of this Cell.
        :type datasheet: str
        """

        self._datasheet = datasheet

    @property
    def anode_chemistry(self) -> str:
        """Gets the anode_chemistry of this Cell.


        :return: The anode_chemistry of this Cell.
        :rtype: str
        """
        return self._anode_chemistry

    @anode_chemistry.setter
    def anode_chemistry(self, anode_chemistry: str):
        """Sets the anode_chemistry of this Cell.


        :param anode_chemistry: The anode_chemistry of this Cell.
        :type anode_chemistry: str
        """

        self._anode_chemistry = anode_chemistry

    @property
    def cathode_chemistry(self) -> str:
        """Gets the cathode_chemistry of this Cell.


        :return: The cathode_chemistry of this Cell.
        :rtype: str
        """
        return self._cathode_chemistry

    @cathode_chemistry.setter
    def cathode_chemistry(self, cathode_chemistry: str):
        """Sets the cathode_chemistry of this Cell.


        :param cathode_chemistry: The cathode_chemistry of this Cell.
        :type cathode_chemistry: str
        """

        self._cathode_chemistry = cathode_chemistry

    @property
    def nominal_capacity(self) -> float:
        """Gets the nominal_capacity of this Cell.

        in what units?  # noqa: E501

        :return: The nominal_capacity of this Cell.
        :rtype: float
        """
        return self._nominal_capacity

    @nominal_capacity.setter
    def nominal_capacity(self, nominal_capacity: float):
        """Sets the nominal_capacity of this Cell.

        in what units?  # noqa: E501

        :param nominal_capacity: The nominal_capacity of this Cell.
        :type nominal_capacity: float
        """

        self._nominal_capacity = nominal_capacity

    @property
    def nominal_cell_weight(self) -> float:
        """Gets the nominal_cell_weight of this Cell.

        in what units?  # noqa: E501

        :return: The nominal_cell_weight of this Cell.
        :rtype: float
        """
        return self._nominal_cell_weight

    @nominal_cell_weight.setter
    def nominal_cell_weight(self, nominal_cell_weight: float):
        """Sets the nominal_cell_weight of this Cell.

        in what units?  # noqa: E501

        :param nominal_cell_weight: The nominal_cell_weight of this Cell.
        :type nominal_cell_weight: float
        """

        self._nominal_cell_weight = nominal_cell_weight