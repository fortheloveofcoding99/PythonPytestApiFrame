
import pytest
import json
import jsonpath
import requests


def test_add_new_datax(): # posten Sie neue datei an der ressource
    app_url = 'https://thetestingworldapi.com/api/studentsDetails'
    file_read = open('../datei/datei1.json','r')
    request_json = json.loads(file_read.read())
    api_response = requests.post(app_url,request_json)
    id = jsonpath.jsonpath(api_response.json(),'id')
    print(id[0])

    tech_api_url = 'https://thetestingworldapi.com/api/technicalskills' # Aktualisieren Sie die datei an der ressource
    file_read1 = open('../datei/techSkill1.json', 'r')
    req_json1 = json.loads(file_read1.read())
    req_json1['id'] = int(id[0])
    req_json1['st_id'] = id[0]
    api_response1 = requests.post(tech_api_url,req_json1)
    print(api_response1.text)

    address_api_url = 'https://thetestingworldapi.com/api/addresses' # Aktualisieren Sie mehr datei on der ressource
    file_read2 = open('../datei/address.json', 'r')
    req2_json = json.loads(file_read2.read())
    req2_json['stId'] = id[0]
    api_response3 = requests.post(address_api_url, req2_json)
    print(api_response3.text)

    final_details_url = 'https://thetestingworldapi.com/api/FinalStudentDetails/'+str(id[0]) # abholen Sie final datei
    api_response4 = requests.get(final_details_url)
    print(api_response4.text)