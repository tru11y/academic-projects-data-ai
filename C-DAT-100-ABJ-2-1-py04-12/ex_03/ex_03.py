import requests
import re

def get_channels(team_id,channel_id):

    token = "eyJ0eXAiOiJKV1QiLCJub25jZSI6IkdKbHhBUWdXRGpzczRLVmdtVVNENG9tMnltY1BmRXhrX2MyR3NycWxZRzgiLCJhbGciOiJSUzI1NiIsIng1dCI6IkhTMjNiN0RvN1RjYVUxUm9MSHdwSXEyNFZZZyIsImtpZCI6IkhTMjNiN0RvN1RjYVUxUm9MSHdwSXEyNFZZZyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC85MDFjYjRjYS1iODYyLTQwMjktOTMwNi1lNWNkMGY2ZDlmODYvIiwiaWF0IjoxNzU4ODMzNzA5LCJuYmYiOjE3NTg4MzM3MDksImV4cCI6MTc1ODgzODMxOSwiYWNjdCI6MCwiYWNyIjoiMSIsImFjcnMiOlsicDEiXSwiYWlvIjoiQVpRQWEvOFpBQUFBUGJrOW85SXhzMDJHbko5NXRLTWJycFBHdUc4V0FEckpVSEJacEtacDhqRnJMTUZnWlVGVzc0eFlOV093U1BCaUg3VCs2WndwUm5oR2hkQlFFU3FLZkJlalcrUjFPUUNNWmlBclNKdkxYM1FmVFJPWkRxdTFHT0dxaHVlblRhb0QxQWptQTA3YWZNLzFUS1N2RU5ETlJKZ25zTG9xMnErMnNNYnpEdG1oaUFVTjNEM0dVRDNOOU5zU1VLclpZdkxaIiwiYW1yIjpbIm1mYSJdLCJhcHBfZGlzcGxheW5hbWUiOiJHcmFwaCBFeHBsb3JlciIsImFwcGlkIjoiZGU4YmM4YjUtZDlmOS00OGIxLWE4YWQtYjc0OGRhNzI1MDY0IiwiYXBwaWRhY3IiOiIwIiwiZmFtaWx5X25hbWUiOiJCYWxsZXkiLCJnaXZlbl9uYW1lIjoiU29scXVlZmxvIiwiaWR0eXAiOiJ1c2VyIiwiaXBhZGRyIjoiNDEuNjYuMzYuMzMiLCJuYW1lIjoiU29scXVlZmxvIEJhbGxleSIsIm9pZCI6IjdhNWQ5YTBmLWI5Y2ItNGFiMi04YTYzLTY4ZjczNDc3ODQ4MyIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS0xNTUyNDM1Mjc3LTE1OTY0OTU3OTUtMzA4OTYxMzczMS01NzU1MyIsInBsYXRmIjoiOCIsInB1aWQiOiIxMDAzMjAwNEM5QjRFQzY2IiwicmgiOiIxLkFYUUF5clFja0dLNEtVQ1RCdVhORDIyZmhnTUFBQUFBQUFBQXdBQUFBQUFBQUFBX0FUaDBBQS4iLCJzY3AiOiJEZXZpY2VNYW5hZ2VtZW50QXBwcy5SZWFkV3JpdGUuQWxsIEdyb3VwLlJlYWQuQWxsIEdyb3VwLlJlYWRXcml0ZS5BbGwgb3BlbmlkIHByb2ZpbGUgVXNlci5SZWFkIGVtYWlsIiwic2lkIjoiMDA3ZTExODktYzYyZC05ZDU2LTM1ZGEtNjYxZGZkODZjZGI4Iiwic2lnbmluX3N0YXRlIjpbImttc2kiXSwic3ViIjoiWWJBN2VoY1pWT2xMeE1sZERud1Bzek5oQWxWZGlMSkNNWTZBd0tkVGJ0TSIsInRlbmFudF9yZWdpb25fc2NvcGUiOiJFVSIsInRpZCI6IjkwMWNiNGNhLWI4NjItNDAyOS05MzA2LWU1Y2QwZjZkOWY4NiIsInVuaXF1ZV9uYW1lIjoic29scXVlZmxvLmJhbGxleUBlcGl0ZWNoLmV1IiwidXBuIjoic29scXVlZmxvLmJhbGxleUBlcGl0ZWNoLmV1IiwidXRpIjoienJiRHN0eVEyMHVtdEdhdTBMWFlBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19jYyI6WyJDUDEiXSwieG1zX2Z0ZCI6InptMHpNN0FjVU5nZVJjb0F6S3NNZWFNZUxHV0h4azNGSnVUU1kyV0hIQkVCWlhWeWIzQmxibTl5ZEdndFpITnRjdyIsInhtc19pZHJlbCI6IjE2IDEiLCJ4bXNfc3NtIjoiMSIsInhtc19zdCI6eyJzdWIiOiJOVm1ZZ0EzN1RBQXFZOXhoSklJNXdQcDB4UTRyZjNqc1VBV19yWFI0UzU0In0sInhtc190Y2R0IjoxNDE3ODA0ODg3LCJ4bXNfdGRiciI6IkVVIn0.RqrK_V8bh63R0Tr0SPjiQ-dkrNR3r1Uyt6et_27LfXmLm26CoqitLu1r69SudV9ICh3wrKLD0EEdTBNXBZiE40pTG7P98KOJ6hvwlJ81OfPZSPAPJHG0uR26ovMarWf1zzEvpP8jqU0I4pYIqTipZdiNLwsvy-qYApf2wbhP9Ks86O4GHY---Jh33q7QQVVK0pBccPh4TOapCu4a1aRkKvvXZG5sAPEkfFkYZbtT50RQ8xoRvBzC0mjPwykwvAEUbGAR2xpt5KEkOtqxn6MRxgPG7he_EzlvhDbENrbG30X8yJEX0JHejJ265_kD7MqgObJg8dICH38l7UMkjXYMYw"
    headers = {
        "Authorization": "Bearer " + token,
        "Accept": "application/json",
    }
    url = f"https://graph.microsoft.com/beta/teams/{team_id}/channels/{channel_id}/messages"
    response = requests.get(url, headers=headers)
    data = response.json()
    data = data["value"]
    # print(data[0]["body"])
    pattern=r"<.*?>"
    replace=""
    dataf={}
    dataf2={}
    dataf3=[]
    for i in range(len(data)):
        dataf["id"]=data[i]["id"]
        dataf["content"]=re.sub(pattern,replace,data[i]["body"]["content"])
        # dataf2[dataf["name"]]=dataf["content"]
        print(dataf["content"])
        # print(dataf["id"])
        # message_id=data["id"]
        for j in range(len(dataf)):
            url2 = f"https://graph.microsoft.com/beta/teams/{team_id}/channels/{channel_id}/messages/{dataf["id"]}/replies"
            response2 = requests.get(url2, headers=headers)
            data2 = response2.json()
            data2 = data2["value"]
            # dataf2["id"]=data2[i]["id"]
            dataf2["content"]=re.sub(pattern,replace,data2[j]["body"]["content"])
            dataf2[dataf["content"]]=dataf2["content"]
            print(dataf2[dataf["content"]])
            # print(dataf2["id"])
    
        # #     dataf[""]
        # # print(data[1]["displayName"])
        # # print(dataf)
        # return dataf2

# get_channels("c0c50c42-eb24-4e6e-b239-7e42537bce26","19:807b053e613e40a28867fe0d5f481c2c@thread.tacv2")

