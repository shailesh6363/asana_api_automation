import requests,json



baseURI="https://app.asana.com/api/1.0/workspaces"
headers={"Authorization":"Bearer "}


def test_get_all_workspaces():
    response = requests.get(baseURI,headers=headers)
    print(response.status_code)