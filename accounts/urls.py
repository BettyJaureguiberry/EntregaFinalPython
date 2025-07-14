from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logged_out/', TemplateView.as_view(template_name='accounts/logged_out.html'), name='logged_out'),
    path('signup/', views.signup_view, name='signup'),
    path('profile/', views.profile_view, name='profile'),
    path('conversation/<int:user_id>/', views.conversation_view, name='conversation'),
    path('start-conversation/', views.start_conversation_view, name='start_conversation'),
    path('edit/', views.edit_profile, name='edit_profile'),

]