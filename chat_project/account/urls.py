from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    # Account stuff
    path('', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),

    # Previous login view
    path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Change password urls
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(),  name='password_change_done'),

    # Reset password urls
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Inbox
    path('inbox/', views.inbox, name='inbox'),

    # Send message
    path('send_message/', views.send_message, name='send_message'),

    #Dump database
    path('dbdump/', views.db_dump, name='db_dump'),
    path('dbdumpfile/', views.db_dump_file, name='db_dump_file'),
]
