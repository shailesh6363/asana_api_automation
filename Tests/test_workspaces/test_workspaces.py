import os
import sys
import allure
import pytest
import requests,json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../utils')))
from API_Modules.api_workspaces  import methods_workspaces
from utils.file_utils import get_test_data_file
from utils.file_utils import get_test_case_data

@allure.title("Get All WorkSapce")
@allure.description("This test case return all the workspaces")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("test_data",get_test_case_data(get_test_data_file('test_data.xlsx'),"workSpace_data",test_case_name="TC1"))
def test_get_all_workspaces(test_data):
    url = test_data["url"]
    endpoints=test_data["endpoint"]
    method = test_data["method"]

    response = methods_workspaces.get_workspaces(method,url,endpoints)
    print(response.status_code)
    assert response.status_code==200
    print(response.json())
    data=response.json()
    assert "data" in data
    pytest.workspace_gid=data['data'][0]['gid']
    assert isinstance(data["data"],list)
    for workspace in data["data"]:
        assert "gid" in workspace
        assert "name" in workspace
        assert "resource_type" in workspace

@allure.title("Get All WorkSapce With Limit")
@allure.description("This test case return all the workspaces with Limit Filter")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("test_data",get_test_case_data(get_test_data_file('test_data.xlsx'),"workSpace_data",test_case_name="TC2"))
def test_get_workspaces_with_limit(test_data):
    url = test_data["url"]
    endpoints=test_data["endpoint"]
    limit=5
    response=methods_workspaces.get_workspace_with_limit(url=url,enidpoint=endpoints,limit=limit)
    print(response.status_code)
    assert response.status_code==200
    data=response.json()
    assert "data" in data
    assert len(data["data"])<=5


@allure.title("Get All WorkSapce with Invalid Limit")
@allure.description("This test case return Error Of Invalid Limit")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("test_data",get_test_case_data(get_test_data_file('test_data.xlsx'),"workSpace_data",test_case_name="TC3"))
def test_get_workspaces_with_invalid_limit(test_data):
    url = test_data["url"]
    endpoints=test_data["endpoint"]
    limit="abc"
    response=methods_workspaces.get_workspace_with_limit(url=url,enidpoint=endpoints,limit=limit)
    print(response.status_code)
    assert response.status_code==400
    data=response.json()
    assert "errors" in data
    print(data)




@allure.title("Add User To WorkSpace")
@allure.description("This test case Add User To WorkSpace")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("test_data",get_test_case_data(get_test_data_file('test_data.xlsx'),"workSpace_data",test_case_name="TC4"))
def test_add_user_to_workspace(test_data):
    url = test_data["url"]
    endpoints=test_data["endpoint"]
    print(endpoints)
    body=test_data["json_body"]
    print(body)
    workspace_gid=pytest.workspace_gid
    print(workspace_gid)
    response=methods_workspaces.add_user_to_workspace(url=url,endpoint=endpoints,workspace_gid=workspace_gid,body=body)
    print(response.status_code)
    print(response.json())
    data= json.loads(response.text)
    print(data)
    assert response.status_code==200
    assert data['data']['gid'] != workspace_gid
    assert data['data']['resource_type'] =='user'
    assert data['data']['is_guest'] == False
    assert data['data']['name'] == 'Shailesh Waghole'
    assert data['data']['email'] == 'shaileshwaghole6363@gmail.com'

