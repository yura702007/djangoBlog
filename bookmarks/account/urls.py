from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # url адреса входа и выхода
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #
    # # url адреса смены пароля
    # path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #
    # # url адреса сброса пароля
    # path(
    #     'password_reset/',
    #     auth_views.PasswordResetView.as_view(),
    #     name='password_reset'
    # ),
    # path(
    #     'password_reset/done/',
    #     auth_views.PasswordResetDoneView.as_view(),
    #     name='password_reset_done'
    # ),
    # path(
    #     'password_reset/<uidb64>/<token>/',
    #     auth_views.PasswordResetConfirmView.as_view(),
    #     name='password_reset_confirm'
    # ),
    # path(
    #     'password_reset/complete/',
    #     auth_views.PasswordResetCompleteView.as_view(),
    #     name='password_reset_complete'
    # ),

    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    # path('login/', views.user_login, name='login'),
]
