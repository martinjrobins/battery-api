import connexion
import six

from swagger_server.models.cell import Cell  # noqa: E501
from swagger_server.models.dataset import Dataset  # noqa: E501
from swagger_server.models.equipment import Equipment  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def get_cell(id):  # noqa: E501
    """get information on a single cell

    Returns information on a cell with the given id.  # noqa: E501

    :param id: Numeric ID of the resource to get
    :type id: int

    :rtype: Cell
    """
    return 'do some magic!'


def get_cells():  # noqa: E501
    """gets information on all cells

    Returns information on all cells.  # noqa: E501


    :rtype: List[Cell]
    """
    return 'do some magic!'


def get_column(id, column_id, precision=None):  # noqa: E501
    """gets a single column of data from a dataset

    Returns a column of a dataset as a binary blob.  # noqa: E501

    :param id: Numeric ID of the resource to get
    :type id: int
    :param column_id: Numeric ID of the column to get
    :type column_id: int
    :param precision: Whether to format the response as a single (32-bit) or double (64-bit) array 
    :type precision: str

    :rtype: str
    """
    return 'do some magic!'


def get_dataset(id):  # noqa: E501
    """get information on a single dataset

    Returns metadata on all the dataset corresponding to the given id.  # noqa: E501

    :param id: Numeric ID of the resource to get
    :type id: int

    :rtype: Dataset
    """
    return 'do some magic!'


def get_datasets():  # noqa: E501
    """gets information on all datasets

    Returns metadata on all the datasets.  # noqa: E501


    :rtype: List[Dataset]
    """
    return 'do some magic!'


def get_equipment(id):  # noqa: E501
    """get information on a single item of test equipment

    Returns information on the test equipment with the given id.  # noqa: E501

    :param id: Numeric ID of the resource to get
    :type id: int

    :rtype: Equipment
    """
    return 'do some magic!'


def get_equipments():  # noqa: E501
    """gets information on all recorded test equipment

    Returns information on all test equipment.  # noqa: E501


    :rtype: List[Equipment]
    """
    return 'do some magic!'


def get_user(id):  # noqa: E501
    """get information on a single user

    Returns information on a user with the given id.  # noqa: E501

    :param id: Numeric ID of the resource to get
    :type id: int

    :rtype: User
    """
    return 'do some magic!'


def get_users():  # noqa: E501
    """gets information on all users

    Returns information on all users.  # noqa: E501


    :rtype: List[User]
    """
    return 'do some magic!'
