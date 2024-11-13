from django.urls import path
from account import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home, name='home'),
    path('login',views.loginview, name='login'),
    path('register',views.registerview, name='register'),
    path('logout',views.loginview, name='logout'),
    path('change_password/', views.change_password, name='change_password'),

   # Forget Password
    path(
        'password_reset/', 
        auth_views.PasswordResetView.as_view(
            template_name='password_reset_form.html'
        ), 
        name='password_reset'
    ),
    path(
        'password_reset_done/', 
        auth_views.PasswordResetDoneView.as_view(
            template_name='password_reset_done.html'
        ), 
        name='password_reset_done'
    ),
    path(
        'password_reset_confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(
            template_name='password_reset_confirm.html'
        ), 
        name='password_reset_confirm'
    ),
    path(
        'password_reset_complete/', 
        auth_views.PasswordResetCompleteView.as_view(
            template_name='password_reset_complete.html'
        ), 
        name='password_reset_complete'
    ),

    #     #Change Password
    # # Password Change
    # path(
    #     'change_password/', 
    #     auth_views.PasswordChangeView.as_view(
    #         template_name='password_change_form.html'
    #     ), 
    #     name='change_password'
    # ),
    # path(
    #     'change_password_done/', 
    #     auth_views.PasswordChangeDoneView.as_view(
    #         template_name='password_change_done.html'
    #     ), 
    #     name='password_change_done'  # This name must match the one used in the view
    # ),
]
