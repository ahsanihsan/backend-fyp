# import json
# import datetime
# import sys
# from django.shortcuts import render
# from django.shortcuts import render, HttpResponse, redirect
# from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
# from jose import jwt
# from django.forms.models import model_to_dict
# # Create your views here.
# # def exception_handler(exctype, value, traceback):
# #     import pdb; pdb.set_trace()
# #     print(value)

# # sys.excepthook = exception_handler

# def index(user):
#     cols=['id','username']
#     users = User.objects.all().values(*cols)
#     users=list(users)
#     return HttpResponse(json.dumps({"error": False, "users": users}), content_type="application/json")

# def sign_up(request):
#     if request.method == "POST":
#         body = json.loads(request.body)
#         email = str(body['email'])
#         fname = str(body['fname'])
#         lname = str(body['lname'])
#         username = str(body['username'])
#         password = str(body['password'])
#         try:
#             if User.objects.filter(email=email).exists():
#                 raise Exception("Key email already exists")
#             user = User.objects.create_user(
#                 first_name=fname, last_name=lname, email=email, username=username)
#             user.set_password(password)
#             user.save()
#         except Exception as e:
#             return HttpResponse(json.dumps({"error": True, "msg": e.message.split('Key')[1]}), content_type="application/json")
#         token = create_token(user)
#         return HttpResponse(json.dumps({"error": False, "auth_token": token}), content_type="application/json")


# def sign_in(request):
#     # import pdb
#     # pdb.set_trace()
#     if request.method == "POST":
#         body = json.loads(request.body)
#         email = str(body['email'])
#         password = str(body['password'])
#         try:
#             username = User.objects.get(email=email).username
#             user = authenticate(username=str(username), password=password)
#         except Exception as e:
#             return HttpResponse(json.dumps({"error": True, "msg": e.message}), content_type="application/json")

#         token = create_token(user)
#         return HttpResponse(json.dumps({"error": False, "auth_token": token}), content_type="application/json")


# def create_token(user):
#     expiry = datetime.date.today() + datetime.timedelta(days=50)
#     return jwt.encode({'id': user.id, 'expiry': expiry.strftime('%s')}, 'seKre8',  algorithm='HS256')
