from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Forgot Password
    path('forgot-password/', views.forgot_password, name='forgot_password'),

    # Restore Password
    path('restore-password/', views.restore_password, name='restore_password'),
]