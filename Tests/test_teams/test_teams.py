import os
import sys
from http.client import responses

import allure
import pytest

from API_Modules.api_teams.methods_teams import get_teams, headers, get_teams_missing_token
from Tests.conftest import get_workspace_Id

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../utils')))
from utils.file_utils import get_test_data_file
from utils.file_utils import get_test_case_data

@allure.title("Get Teams - Valid Workspace ID")
@allure.description("Verify that the API returns a list of teams for a valid workspace ID")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("test_data", get_test_case_data(get_test_data_file('test_data.xlsx'), "teams", test_case_name="TC1"))
def test_get_all_teams(test_data,get_workspace_Id):
    url = test_data["url"]
    endpoints=test_data["endpoint"]
    workspace_id=pytest.workspace_gid
    response=get_teams(url=url,endpoint=endpoints,workspace_gid=workspace_id)
    assert response.status_code == 200
    data=response.json()
    print(data)
    assert data['data'][0]['name']=="IT"
    assert data['data'][0]['resource_type']=="team"


@allure.title("Get Teams - Invalid Workspace ID")
@allure.description("Verify that the API returns an error for an invalid workspace ID")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("test_data", get_test_case_data(get_test_data_file('test_data.xlsx'), "teams", test_case_name="TC2"))
def test_get_teams_invalid_workspace_id(test_data,get_workspace_Id):
    url = test_data["url"]
    endpoints=test_data["endpoint"]
    workspace_id=1234
    response=get_teams(url=url,endpoint=endpoints,workspace_gid=workspace_id)
    assert response.status_code == 404



@allure.title("Get Teams - Missing Authentication Token")
@allure.description("Verify that the API returns an error when the authentication token is missing")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("test_data", get_test_case_data(get_test_data_file('test_data.xlsx'), "teams", test_case_name="TC3"))
def test_get_teams_invalid_token(test_data,get_workspace_Id):
    url = test_data["url"]
    endpoints=test_data["endpoint"]
    workspace_id=pytest.workspace_gid
    response=get_teams_missing_token(url=url,endpoint=endpoints,workspace_gid=workspace_id)
    assert response.status_code == 401