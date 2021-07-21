import openapi_client
import urllib3
import json

def login(host, username, password):
    configuration = openapi_client.Configuration()
    configuration.host = host
    configuration.username = username
    configuration.password = password

    # create an instance of the API class
    api_client = openapi_client.ApiClient(configuration)

    headers = urllib3.util.make_headers(
        basic_auth=(
            configuration.username + ':' + configuration.password
        )
    )

    login_response = json.loads(
        api_client.request(
            'POST', configuration.host + '/login',
            headers=headers
        ).data
    )

    if 'access_token' not in login_response:
        raise RuntimeError('login failed')

    return login_response['access_token']


