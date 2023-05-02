from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('works/', views.WorkList.as_view()),
    path('works/<int:pk>/', views.WorkDetail.as_view()),
    path('register/', views.RegisterUser.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)