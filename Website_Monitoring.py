import requests
response = requests.get('https://www.daraz.pk/')
print(response.status_code)