from django.urls import path
from . import views
#from .views import SampleAppList


urlpatterns = [
    path('', views.SampleAppList.as_view()),
    path('smaple', views.post_list, name='post_list'),
]
