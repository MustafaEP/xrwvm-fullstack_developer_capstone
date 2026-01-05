# Uncomment the imports below before you add the function code
# import requests
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

def get_request(endpoint, **kwargs):
    params = ""
    if(kwargs):
        for key,value in kwargs.items():
            params=params+key+"="+value+"&"

    request_url = backend_url+endpoint+"?"+params

    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except:
        # If any error occurs
        print("Network exception occurred")

def analyze_review_sentiments(review_text):
    try:
        response = requests.post(
            sentiment_analyzer_url,
            json={"text": review_text}
        )
        return response.json()
    except:
        return {"sentiment": "neutral"}




def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(
            request_url,
            data=json.dumps(data_dict),
            headers={"Content-Type": "application/json"},
            timeout=5
        )
        print("STATUS:", response.status_code)
        print("BODY:", response.text)
        return response.json()
    except Exception as e:
        print("POST REVIEW ERROR:", e)
        return None



