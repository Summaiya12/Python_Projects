import requests
url = "https://www.google.com/"
timeout = 1
while True:
    try:
        requests = requests.get(url,timeout = timeout)
        print("Connected")
    except:
        print("Not Connected")