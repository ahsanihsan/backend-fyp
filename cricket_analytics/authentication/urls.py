from django.conf.urls import include,url
from . import views
urlpatterns = [
   url("/",views.index),
   url("sign_up",views.sign_up),
   url("sign_in",views.sign_in),

]