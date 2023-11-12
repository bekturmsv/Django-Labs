from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login/', views.AuthLoginView.as_view(), name='login'),
    path('logout/', views.AuthLogoutView.as_view(), name='logout'),
    path('user_list/', views.PostView.as_view(), name='post'),
]