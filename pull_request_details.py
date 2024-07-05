# to get username and their id

# import requests

# uri = 'https://api.github.com/repos/kubernetes/kubernetes/pulls'
# response = requests.get(uri)

# response_json = response.json()
# if response.status_code == 200:
#     for i in range(len(response_json)):
#         print("user:",response_json[i]["user"]["login"], "id:",response_json[i]["user"]["id"]) 
# else:
#     print(f"Sorry, we got {response.status_code} ")

#===============

# Program to demonstrate integration with GitHub to fetch the 
# details of Users who created Pull requests(Active) on Kubernetes Github repo.


# to get username and pr count

import requests

uri = 'https://api.github.com/repos/kubernetes/kubernetes/pulls'

response = requests.get(uri)
response_json = response.json()
pull_req_list = {}

if response.status_code == 200:

    for i in range(len(response_json)):  
        username = response_json[i]["user"]["login"]
        if username in pull_req_list:
            pull_req_list[username] += 1;
        else:
            pull_req_list[username]  = 1;  
    print("Username and pull request count")

    for creator, count in pull_req_list.items():
        print(f"{creator}: {count} PR(s)")
else:
    print(f"Something went wrong, got {response.status_code} as response,")