import requests


def get_channels(team_id):

    token = "eyJ0eXAiOiJKV1QiLCJub25jZSI6IjByZnM4LTFfWmpVaDUwNFJIWk8zZFlrdkN0TEkzeVBaV3NaeGYzdFRTMlEiLCJhbGciOiJSUzI1NiIsIng1dCI6IkhTMjNiN0RvN1RjYVUxUm9MSHdwSXEyNFZZZyIsImtpZCI6IkhTMjNiN0RvN1RjYVUxUm9MSHdwSXEyNFZZZyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC85MDFjYjRjYS1iODYyLTQwMjktOTMwNi1lNWNkMGY2ZDlmODYvIiwiaWF0IjoxNzU4ODEyOTQyLCJuYmYiOjE3NTg4MTI5NDIsImV4cCI6MTc1ODgxODM3OCwiYWNjdCI6MCwiYWNyIjoiMSIsImFjcnMiOlsicDEiXSwiYWlvIjoiQVpRQWEvOFpBQUFBcDl1eldDZFRXQlQ5aFQyS3pDTkM2WmowL3JjZGF2NWxvRVREMkI4NHp5YzJQTk5wOHEyb2IzVjgzelkrUFFldWNvZmtQTTNmNXhFaDBYNkc2bXJWdjhUZlpJRFUxS3FFL2J6RDZpZmxZcDQxbVFRbm10Y3ZMaWtFUldMcmZtMlE3SUN6NnAyNWdPOEo5M1hkMkVrVjlDaWJOdlA1R0F4VlJnOGx5Z0xpaVVZUjZhUDBjQlV0eGVNQlQ4S0pEWWdYIiwiYW1yIjpbIm1mYSJdLCJhcHBfZGlzcGxheW5hbWUiOiJHcmFwaCBFeHBsb3JlciIsImFwcGlkIjoiZGU4YmM4YjUtZDlmOS00OGIxLWE4YWQtYjc0OGRhNzI1MDY0IiwiYXBwaWRhY3IiOiIwIiwiZmFtaWx5X25hbWUiOiJCYWxsZXkiLCJnaXZlbl9uYW1lIjoiU29scXVlZmxvIiwiaWR0eXAiOiJ1c2VyIiwiaXBhZGRyIjoiNDEuNjYuMzYuMzMiLCJuYW1lIjoiU29scXVlZmxvIEJhbGxleSIsIm9pZCI6IjdhNWQ5YTBmLWI5Y2ItNGFiMi04YTYzLTY4ZjczNDc3ODQ4MyIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS0xNTUyNDM1Mjc3LTE1OTY0OTU3OTUtMzA4OTYxMzczMS01NzU1MyIsInBsYXRmIjoiOCIsInB1aWQiOiIxMDAzMjAwNEM5QjRFQzY2IiwicmgiOiIxLkFYUUF5clFja0dLNEtVQ1RCdVhORDIyZmhnTUFBQUFBQUFBQXdBQUFBQUFBQUFBX0FUaDBBQS4iLCJzY3AiOiJEZXZpY2VNYW5hZ2VtZW50QXBwcy5SZWFkV3JpdGUuQWxsIEdyb3VwLlJlYWQuQWxsIEdyb3VwLlJlYWRXcml0ZS5BbGwgb3BlbmlkIHByb2ZpbGUgVXNlci5SZWFkIGVtYWlsIiwic2lkIjoiMDA3ZTExODktYzYyZC05ZDU2LTM1ZGEtNjYxZGZkODZjZGI4Iiwic2lnbmluX3N0YXRlIjpbImttc2kiXSwic3ViIjoiWWJBN2VoY1pWT2xMeE1sZERud1Bzek5oQWxWZGlMSkNNWTZBd0tkVGJ0TSIsInRlbmFudF9yZWdpb25fc2NvcGUiOiJFVSIsInRpZCI6IjkwMWNiNGNhLWI4NjItNDAyOS05MzA2LWU1Y2QwZjZkOWY4NiIsInVuaXF1ZV9uYW1lIjoic29scXVlZmxvLmJhbGxleUBlcGl0ZWNoLmV1IiwidXBuIjoic29scXVlZmxvLmJhbGxleUBlcGl0ZWNoLmV1IiwidXRpIjoiaXhENmp2OXFpRWVIRlQwZkx3dENBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19jYyI6WyJDUDEiXSwieG1zX2Z0ZCI6ImFZR1RPcjlvVUJPaF9iYTdQNk92ZGxkTG9SbWd3bzBKeUVoUlhBMjhTam9CWlhWeWIzQmxkMlZ6ZEMxa2MyMXoiLCJ4bXNfaWRyZWwiOiI0IDEiLCJ4bXNfc3NtIjoiMSIsInhtc19zdCI6eyJzdWIiOiJOVm1ZZ0EzN1RBQXFZOXhoSklJNXdQcDB4UTRyZjNqc1VBV19yWFI0UzU0In0sInhtc190Y2R0IjoxNDE3ODA0ODg3LCJ4bXNfdGRiciI6IkVVIn0.PjrksYlfD1bioHKomyez5X_0gqT3Bs4bvhVKBJmfsALkCf4LxlbA7OydsA51MG5-ANNPq8hjLRYqSs_G5pKBbvvbtwUSMvLXJiXUZs9eJMt5WzlC320rG_RRvDS-cEutfOOm3B1Jgf_13CfxP-2ydw8Sj3c8Xx-2OKBpyw5wt89aF-CWllT6sIyMKX1kR1mQum-Fjgk6svqcFCEybj4CKRX_tArKMxI7GvjQo8QtkRNAkBqyzW_4FbC-QjhX1D6dUKfjvvmFZnKe4r9UEUVO2QWV0dpudN0BdktPMJ5aSpqveGLgf4c4ssOYMjqqZmZneNCSFsUKQ0_WU0Di_LyXIA"
    headers = {
        "Authorization": "Bearer " + token,
        "Accept": "application/json",
    }
    url = f"https://graph.microsoft.com/beta/teams/{team_id}/channels"
    response = requests.get(url, headers=headers)
    data = response.json()
    data = data["value"]
    # print(data)
    # return data[0]
    dataf = []
    dataf2 = {}
    for i in range(len(data)):
        # dataf["id"] = data[i]["id"]
        dataf.append( data[i]["displayName"])
        # dataf2[dataf["id"]] = dataf["name"]
        # print(i)

    #     dataf[""]
    # print(data[1]["displayName"])
    # print(dataf)
    return dataf

# get_channels("c0c50c42-eb24-4e6e-b239-7e42537bce26")
# channels = get_channels("c0c50c42-eb24-4e6e-b239-7e42537bce26")
# for channel in channels:
#     print(channel)
