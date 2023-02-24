import os
import requests
import json
from .tokens import account_activation_token
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_str, force_bytes



API_KEY = os.environ.get("MG_API_KEY")
BASE_URL = os.environ.get("MG_BASE_URL")





def send_token(user, email):
    
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = account_activation_token.make_token(user)
    url = f"http://localhost:8000/activate/{uid}/{token}"

    response = requests.post(f"https://api.mailgun.net/v3/{BASE_URL}/messages",auth=("api", API_KEY),data={"from": f"mailgun@{BASE_URL}","to": email,"subject": "Hello",
            "template": "emailconfirm",
			"t:variables": json.dumps({"URL": url})})

  

    print(response.text)
    



    
   

