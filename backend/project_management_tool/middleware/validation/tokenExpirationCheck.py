from authlib import jose
from datetime import datetime
import os
from dotenv import load_dotenv

def isTokenExpired(request):
    authorization_header = request.META.get('HTTP_AUTHORIZATION')

    if authorization_header:
        public = os.getenv('PUBLIC_KEY')
        token = authorization_header.split(' ')[1]
        decoded_token = jose.jwt.decode(token,key=public)
        
        expiration_time = decoded_token['exp']
        
        current_time = datetime.utcnow().timestamp()
        if current_time < expiration_time:
            return True
        else:
            return False

    else:
        print("Error, no Authorization Header included.")
        return True