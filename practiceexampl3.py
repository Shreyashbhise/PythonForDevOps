import requests

service_url = 'https://example.com'

expected_status_code = 200

def check_service_status(url,expected_code):
    try:
        response = requests.get(url)
        if response.status_code == expected_code:
            return True
        else:
             return False
    except requests.exceptions.RequestException:
        return False
if check_service_status(service_url,expected_status_code):
    print("The service at {} is up and running.".format(service_url))
else:
    print("The service at {} is up and running.".format(service_url))