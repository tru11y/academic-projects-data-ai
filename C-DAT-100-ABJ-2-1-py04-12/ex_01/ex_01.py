import requests


def member_of():
    token = "eyJ0**********************************************************************************************************************************************M"
    headers = {
        "Authorization": "Bearer "+token,
        "Accept": "application/json",
    }
    url = "https://graph.microsoft.com/beta/me/memberOf"
    response = requests.get(url, headers=headers)
    data=response.json()
    data=data["value"]
    # return data[0]
    dataf={}
    dataf2={}
    for i in range(len(data)):
        dataf["id"]=data[i]["id"]
        dataf["name"]=data[i]["displayName"]
        dataf2[dataf["id"]]=dataf["name"]
        # print(i)

    #     dataf[""]
    # print(data[1]["displayName"])
    # print(dataf)
    return dataf2


# member_of()


# teams = member_of ()
# for name , id in teams.items() :
#     print ( name )
#     print ( id )
