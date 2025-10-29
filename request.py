import requests

response = requests.get("https://github.com/kaavyakaavya390/my_first_package")
# print(response.content)
# print(response.headers)
print(response.status_code)
