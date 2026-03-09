import requests


def member_of():
    token = "eyJ0eXAiOiJKV1QiLCJub25jZSI6Ik9GdzJaRnRuZGxuWFVzWXBQYWhUdGItNThZX0tCRWZQanZ2S0JQTEpyejgiLCJhbGciOiJSUzI1NiIsIng1dCI6IkhTMjNiN0RvN1RjYVUxUm9MSHdwSXEyNFZZZyIsImtpZCI6IkhTMjNiN0RvN1RjYVUxUm9MSHdwSXEyNFZZZyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC85MDFjYjRjYS1iODYyLTQwMjktOTMwNi1lNWNkMGY2ZDlmODYvIiwiaWF0IjoxNzU4ODAwNjQxLCJuYmYiOjE3NTg4MDA2NDEsImV4cCI6MTc1ODgwNDgwOCwiYWNjdCI6MCwiYWNyIjoiMSIsImFjcnMiOlsicDEiXSwiYWlvIjoiQVpRQWEvOFpBQUFBbnJpMGh1Z3pNZ2xCZ2Rma2VQanNJeDJFbE50OXVBUVgrWU1md1c3WFdQVHRkNmt3dHVIK3hndStKU2hqNG5NQS9vQlhnUFVFR3c0OGE2N0oyQ2lJVEF6QVBKMnYyTlZVekhuN2lVVndzWlptc28zVXQvSmsxVndzWEkzeXRXOFFPTXlTcDhPUWE1eUs0ZVBXQ29NMGltQ3dqOG9mcU1FbDBNSWJCdU9tVGZ6ZHMyTWpHWkFoUG90dVdrUnVaOHlzIiwiYW1yIjpbIm1mYSJdLCJhcHBfZGlzcGxheW5hbWUiOiJHcmFwaCBFeHBsb3JlciIsImFwcGlkIjoiZGU4YmM4YjUtZDlmOS00OGIxLWE4YWQtYjc0OGRhNzI1MDY0IiwiYXBwaWRhY3IiOiIwIiwiZmFtaWx5X25hbWUiOiJCYWxsZXkiLCJnaXZlbl9uYW1lIjoiU29scXVlZmxvIiwiaWR0eXAiOiJ1c2VyIiwiaXBhZGRyIjoiNDEuNjYuMzYuMzMiLCJuYW1lIjoiU29scXVlZmxvIEJhbGxleSIsIm9pZCI6IjdhNWQ5YTBmLWI5Y2ItNGFiMi04YTYzLTY4ZjczNDc3ODQ4MyIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS0xNTUyNDM1Mjc3LTE1OTY0OTU3OTUtMzA4OTYxMzczMS01NzU1MyIsInBsYXRmIjoiOCIsInB1aWQiOiIxMDAzMjAwNEM5QjRFQzY2IiwicmgiOiIxLkFYUUF5clFja0dLNEtVQ1RCdVhORDIyZmhnTUFBQUFBQUFBQXdBQUFBQUFBQUFBX0FUaDBBQS4iLCJzY3AiOiJEZXZpY2VNYW5hZ2VtZW50QXBwcy5SZWFkV3JpdGUuQWxsIEdyb3VwLlJlYWQuQWxsIEdyb3VwLlJlYWRXcml0ZS5BbGwgb3BlbmlkIHByb2ZpbGUgVXNlci5SZWFkIGVtYWlsIiwic2lkIjoiMDA3ZTExODktYzYyZC05ZDU2LTM1ZGEtNjYxZGZkODZjZGI4Iiwic2lnbmluX3N0YXRlIjpbImttc2kiXSwic3ViIjoiWWJBN2VoY1pWT2xMeE1sZERud1Bzek5oQWxWZGlMSkNNWTZBd0tkVGJ0TSIsInRlbmFudF9yZWdpb25fc2NvcGUiOiJFVSIsInRpZCI6IjkwMWNiNGNhLWI4NjItNDAyOS05MzA2LWU1Y2QwZjZkOWY4NiIsInVuaXF1ZV9uYW1lIjoic29scXVlZmxvLmJhbGxleUBlcGl0ZWNoLmV1IiwidXBuIjoic29scXVlZmxvLmJhbGxleUBlcGl0ZWNoLmV1IiwidXRpIjoiNG9qZDl1SlZ4MC1aUEJYS2JQdFhBUSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19jYyI6WyJDUDEiXSwieG1zX2Z0ZCI6Ik5yMUVDbVBfUTFWX2poNFItU0V0dGtzQklscDhzNmlMbjFCS2NWTEhQNllCWm5KaGJtTmxZeTFrYzIxeiIsInhtc19pZHJlbCI6IjEgMjQiLCJ4bXNfc3NtIjoiMSIsInhtc19zdCI6eyJzdWIiOiJOVm1ZZ0EzN1RBQXFZOXhoSklJNXdQcDB4UTRyZjNqc1VBV19yWFI0UzU0In0sInhtc190Y2R0IjoxNDE3ODA0ODg3LCJ4bXNfdGRiciI6IkVVIn0.TiQyZZbUOAIqPok450EksQE9yKYxkcVa1uDnYR9Rfao1AlpsKl2ldtgayfT23VdOtGxaMViBa9pXTL1xpbUyZFdSpPa_bilnTs-a-sssXkOm7Q1oN8f5shEXnq4UJX_zlzq38Awa5BjB30gDXt3qZWwugsMYUFY_FRzqCVHUZRRm9DlswGfHRUr-dghYPETQy_HjyosinsbyZMne7tbYICTWosiZFSOMFtf1xqegb-C4y7_kMrLwOKnFbmNBmMPlEDx8olojhLXf-DBpAbgWMqq298rmmzyHyUbumocKQLRcB6Luvq51wSKrVlB1V_EZG2Dq0SmksQR0GpLvgCc7aw"
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
