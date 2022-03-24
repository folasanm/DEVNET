import requests

url = "https://webexapis.com/v1/teams"

payload={}
headers = {
  'Authorization': 'Bearer ZTEyNzFiNzUtOTEwNy00MjU2LTg5NzEtYWM4MDczY2UzZDBiNTRhNDMxNmUtZGI1_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
