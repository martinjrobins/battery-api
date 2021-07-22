import openapi_client
from openapi_client.api import users_api
from openapi_client.login import login
from pprint import pprint
import numpy as np


token = \
'''eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyNjk0MzUxOSwianRpIjoiOTE1ZDVjNzUtNmRlMS00MjI5LTk2NGEtYTg4Yzc2ZmJhOGI5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IntcImlkXCI6IDEsIFwidXNlcm5hbWVcIjogXCJib2JcIiwgXCJlbWFpbFwiOiBcImJvYkBnbWFpbC5jb21cIn0iLCJuYmYiOjE2MjY5NDM1MTksImNzcmYiOiI0NmQ0NzljNC1hMTA2LTQzZmItYTNkNi1hNjZiNzg3NjdkZTkiLCJleHAiOjE2MjY5NDcxMTl9.qLLq-6q4Nf9pWBME_AD50H4QkGnJEaNtlj4M4YUdxHw'''

configuration = openapi_client.Configuration(
    host="http://localhost:5001/api",
    access_token=token
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)

    # gets information on all datasets
    api_response = api_instance.get_datasets()
    pprint(api_response)

    # get a single column
    id = 18
    column_id = 224
    api_response = api_instance.get_column(18, 224)
    numpy_array = np.frombuffer(api_response.read(), dtype=np.float32)
