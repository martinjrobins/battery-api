# swagger_client.UsersApi

All URIs are relative to *https://virtserver.swaggerhub.com/martinjrobins/battery-api/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cell**](UsersApi.md#get_cell) | **GET** /cell/{id} | get information on a single cell
[**get_cells**](UsersApi.md#get_cells) | **GET** /cell | gets information on all cells
[**get_column**](UsersApi.md#get_column) | **GET** /dataset/{id}/{column_id} | gets a single column of data from a dataset
[**get_dataset**](UsersApi.md#get_dataset) | **GET** /dataset/{id} | get information on a single dataset
[**get_datasets**](UsersApi.md#get_datasets) | **GET** /dataset | gets information on all datasets
[**get_equipment**](UsersApi.md#get_equipment) | **GET** /equipment/{id} | get information on a single item of test equipment
[**get_equipments**](UsersApi.md#get_equipments) | **GET** /equipment | gets information on all recorded test equipment
[**get_user**](UsersApi.md#get_user) | **GET** /user/{id} | get information on a single user
[**get_users**](UsersApi.md#get_users) | **GET** /user | gets information on all users

# **get_cell**
> Cell get_cell(id)

get information on a single cell

Returns information on a cell with the given id. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 56 # int | Numeric ID of the resource to get

try:
    # get information on a single cell
    api_response = api_instance.get_cell(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_cell: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric ID of the resource to get | 

### Return type

[**Cell**](Cell.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cells**
> list[Cell] get_cells()

gets information on all cells

Returns information on all cells. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))

try:
    # gets information on all cells
    api_response = api_instance.get_cells()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_cells: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Cell]**](Cell.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_column**
> str get_column(id, column_id, precision=precision)

gets a single column of data from a dataset

Returns a column of a dataset as a binary blob. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 56 # int | Numeric ID of the resource to get
column_id = 56 # int | Numeric ID of the column to get
precision = 'single' # str | Whether to format the response as a single (32-bit) or double (64-bit) array  (optional) (default to single)

try:
    # gets a single column of data from a dataset
    api_response = api_instance.get_column(id, column_id, precision=precision)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_column: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric ID of the resource to get | 
 **column_id** | **int**| Numeric ID of the column to get | 
 **precision** | **str**| Whether to format the response as a single (32-bit) or double (64-bit) array  | [optional] [default to single]

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset**
> Dataset get_dataset(id)

get information on a single dataset

Returns metadata on all the dataset corresponding to the given id. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 56 # int | Numeric ID of the resource to get

try:
    # get information on a single dataset
    api_response = api_instance.get_dataset(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric ID of the resource to get | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datasets**
> list[Dataset] get_datasets()

gets information on all datasets

Returns metadata on all the datasets. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))

try:
    # gets information on all datasets
    api_response = api_instance.get_datasets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_datasets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Dataset]**](Dataset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_equipment**
> Equipment get_equipment(id)

get information on a single item of test equipment

Returns information on the test equipment with the given id. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 56 # int | Numeric ID of the resource to get

try:
    # get information on a single item of test equipment
    api_response = api_instance.get_equipment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_equipment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric ID of the resource to get | 

### Return type

[**Equipment**](Equipment.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_equipments**
> list[Equipment] get_equipments()

gets information on all recorded test equipment

Returns information on all test equipment. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))

try:
    # gets information on all recorded test equipment
    api_response = api_instance.get_equipments()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_equipments: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Equipment]**](Equipment.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(id)

get information on a single user

Returns information on a user with the given id. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 56 # int | Numeric ID of the resource to get

try:
    # get information on a single user
    api_response = api_instance.get_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric ID of the resource to get | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> list[User] get_users()

gets information on all users

Returns information on all users. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))

try:
    # gets information on all users
    api_response = api_instance.get_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[User]**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

