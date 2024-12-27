from django.urls import path
from . import views
urlpatterns=[
    path('insert',views.insert),
    path('signupform',views.signupform),
    path('signin',views.signin),
    path('signincode',views.signincode),
    path('index',views.index),
    path('Electronics',views.Electronics),
    path('cart',views.cart_detail),
    path('add-to-cartfirst/<int:id>/',views.add_to_cartfirst,name='add-to-cartfirst'),
    path('cart_detail',views.cart_detail),
    path('add/<int:id>/',views.add_item,name='add'),
    path('remove/<int:id>/',views.remove_item,name='remove'),
    path('cart_detail/<int:id>',views.cart_detail),
    path('updated_cart',views.updated_cart),
    path('updated_cart1',views.updated_cart1),
    path('checkout',views.check_out,name='checkout'),
    path('sessiondetails',views.get_session_details,name='sessiondetails'),
    path('adminpage',views.admin_page,name='adminpage'),
    path('clear',views.clear,name='clear'),
]
