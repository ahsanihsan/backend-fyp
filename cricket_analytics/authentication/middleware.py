from datetime import datetime
from jose import jwt
from django.contrib.auth.models import User

class Authenticate(object):
    def process_request(self, request):
        if 'HTTP_AUTHORIZATION' in request.META:
            token =request.META['HTTP_AUTHORIZATION']
            request.current_user = User.objects.get(id = jwt.decode(token, 'seKre8')['id'])