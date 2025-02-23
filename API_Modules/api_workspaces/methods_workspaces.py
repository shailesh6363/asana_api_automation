import requests
from utils.file_utils import get_test_case_data
from utils import config_parser
from utils.config_parser import get_token


headers={"Content-Type":'application/json',"Authorization":"Bearer {token}".format(token=get_token())}


print(headers)

def get_workspaces(method,url,endpoint):
    response=requests.get(url=url+endpoint, headers=headers,params=None)

    return response

def get_workspace_with_limit(url,enidpoint,limit):
    response=requests.get(url=url+enidpoint+"?opt_fields=&limit={limits}".format(limits=limit), headers=headers)

    return response


def add_user_to_workspace(url,endpoint,workspace_gid,body):
    endpoint=endpoint.format(workspace_gid=workspace_gid)
    response=requests.post(url=url+endpoint, headers=headers,json=body)

    return response