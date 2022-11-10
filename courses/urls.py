from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name="index"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", LoginUser.as_view(), name="login"),
    path("register/", RegisterUser.as_view(), name="register"),
    path('catalog/', AllCoursesView.as_view(), name="catalog"),
    path('learn/', LearnCoursesView.as_view(), name="learn"),
    path('control/', control_page, name="control"),
    path('update/<int:pk>/', update_page, name='update_page'),
    path('delete/<int:pk>/', delete_page, name='delete_page'),
    path('catalog/<int:pk>/', DetailCourseView.as_view(), name='course-detail'),
    path('subscribe/<int:pk>/', subscribe, name='subscribe'),
    path('unsubscribe/<int:pk>/', unsubscribe, name='unsubscribe'),
]