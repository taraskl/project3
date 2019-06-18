from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('signup/', views.signup_view, name='signup'),
    path('menu/', views.menu_view, name='menu'),
    path('cart/', views.cart_view, name='cart'),
    path('success/', views.success_view, name='success'),
    path('orders/', views.orders_view, name='orders'),
]
