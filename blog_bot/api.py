import requests
import json
from pprint import pprint as pp

url = "https://blog-api-2h5h.onrender.com/api/v1/posts/"

payload = ""
headers = {
    'Authorization': 'Basic YWRtaW46MTIzNA=='
}


def get_posts():
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        my_json = json.loads(response.text)
        return my_json
    except Exception as e:
        return [{"title": "Nice Try!", "content": "Ma'lumot qo'shing"}]
