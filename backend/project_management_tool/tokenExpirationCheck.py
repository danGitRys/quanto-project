from authlib import jose
from datetime import datetime
import os
from dotenv import load_dotenv

def isTokenExpired(token):
    try:
        public = os.getenv('PUBLIC_KEY')
        decoded_token = jose.jwt.decode(token,key=public)
        print(token)
        expiration_time = decoded_token['exp']

        current_time = datetime.utcnow().timestamp()
        if current_time > expiration_time:
            print("Token has expired.")
        else:
            print("Token is still valid.")

    except jose.jwt.ExpiredSignatureError:
        print("Token has expired.")
    except jose.jwt.InvalidTokenError:
        print("Invalid token.")