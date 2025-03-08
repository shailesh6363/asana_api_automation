import requests
from utils.file_utils import get_test_case_data
from utils import config_parser
from utils.config_parser import get_token


headers={"Content-Type":'application/json',"Authorization":"Bearer {token}".format(token=get_token())}
headers_invalid_token={"Content-Type":'application/json',"Authorization":"Bearer "}



def get_teams(url,endpoint,workspace_gid):
    endpoint=endpoint.format(workspace_gid=workspace_gid)
    print(url)
    print(endpoint)
    response=requests.get(url=url+endpoint,headers=headers,params=None)

    return response



def get_teams_missing_token(url,endpoint,workspace_gid):
    endpoint=endpoint.format(workspace_gid=workspace_gid)
    print(url)
    print(endpoint)
    response=requests.get(url=url+endpoint,headers=headers_invalid_token,params=None)

    return response