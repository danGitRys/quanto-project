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
        print(decoded_token)
        
        expiration_time = decoded_token['exp']
        print(expiration_time)

        current_time = datetime.utcnow().timestamp()
        print(current_time)
        if current_time < expiration_time:
            print("True")
            return True

        else:
            print("False")
            return False

    else:
        print("Error, no Authorization Header included.")
        return True