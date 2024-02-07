
import json
import jsonpath
import pytest
import requests

def test_add_new_datay(): # posten Sie neue datei an der ressource
    global id
    app_url = 'https://thetestingworldapi.com/api/studentsDetails'
    file_read = open('../datei/datei1.json','r')
    request_json = json.loads(file_read.read())
    api_response = requests.post(app_url,request_json)
    id = jsonpath.jsonpath(api_response.json(),'id')
    print(id[0])
    #print(api_response.elapsed)

def test_details_abholen(): # um die datei zu abholen
    final_details_url = 'https://thetestingworldapi.com/api/FinalStudentDetails/'+str(id[0]) # abholen Sie final datei
    api_response5 = requests.get(final_details_url)
    print(api_response5.text)