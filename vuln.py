import requests

data = requests.get("https://www.educative.io/", verify = False)
print(data.status_code)
