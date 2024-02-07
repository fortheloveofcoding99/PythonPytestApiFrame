
import requests
from requests.auth import HTTPBasicAuth

def test_with_basic_auth():
    response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('somsarkar9698@gmail.com','Somnathsarkar@123'))
    print(response.text)

def test_oauth_api():
    auth_url = 'https://thetestingworldapi.com/Help/api/StDetails/10065099'
    response1 = requests.get(auth_url)
    print(response1.text)