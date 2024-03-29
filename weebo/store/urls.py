from django.urls import path
from . import views


urlpatterns = [
    path('',views.store,name='store'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('update_item',views.updateItem,name='update_item'),
    path('process_order',views.processOrder,name='process_order'), 
    path('login',views.loginpage,name='login'),
    path('logout',views.logoutUser,name='logout'),
    path('register',views.register,name="register"),
    path('myorder',views.myOrder,name="myorder"),
]
