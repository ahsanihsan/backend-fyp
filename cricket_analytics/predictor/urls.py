from django.conf.urls import include,url
from . import views
urlpatterns = [
   url("who_will_win",views.who_will_win),
   url("score_of_teams",views.score_of_teams),
   url("runrate",views.runrate),
   url("will_batsman_get_out",views.will_batsman_get_out),
   url("what_score_will_batsman_make",views.what_score_will_batsman_make),

]