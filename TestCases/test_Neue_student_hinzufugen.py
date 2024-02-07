import jsonpath
import requests
import pytest
import json


def test_add_student_data():
    api_url = 'https://thetestingworldapi.com/api/studentsDetails'
    file = open('datei/datei1.json','r') #lesen Sie die json datei in der verzeichnis
    json_request = json.loads(file.read()) # laden Sie die datei
    api_respose = requests.post(api_url,json_request) # sammeln Sie die antwort
    print(api_respose.text) # drucken Sie die antwort dass Sie erhalten habe
    #pytest TestCases -s  > to run the above test case

def test_get_student_data():
    api_url = 'https://thetestingworldapi.com/api/studentsDetails/10065013'
    api_response = requests.get(api_url)
    json_response = json.loads(api_response.text) # typecasting the api response to json response
    id = jsonpath.jsonpath(json_response,'data.id') # sammeln die wert des ids von der json response
#    assert id[0] == 10065013

def test_update_student_data():
    api_url = 'https://thetestingworldapi.com/api/studentsDetails/10065013'
    file = open('ApiTestProject/datei/datei1.json','r') #lesen Sie die json datei in der verzeichnis
    json_request = json.loads(file.read())  # laden Sie die datei
    api_respose = requests.put(api_url,json_request) # sammeln Sie die antwort
    print(api_respose.text) # drucken Sie die antwort dass Sie erhalten habe
    #pytest TestCases -s  > to run the above test case

def test_update_student_data():
    api_url = 'https://thetestingworldapi.com/api/studentsDetails/10065014'
    api_response = requests.delete(api_url)
    print(api_response.text)
    print(api_response.status_code)