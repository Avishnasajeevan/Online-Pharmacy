from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home,name='home'),
    path('<str:name>/', views.homeView, name='homecat'),  #CREATED URL FOR EACH CATEGORIES
    path('<str:cname>/<str:pname>/',views.productinfo, name='productinfo'), #FOR EACH PRODUCT INFO BY CATGORY
    path('about', views.about),
    path('faq', views.faq),
    path('reg', views.reg),
    path('cart', views.cart_page, name='cart'),
    path('addtocart', views.add_to_cart, name='addtocart'),
    path('remove_cart/<str:cid>', views.remove_cart, name='remove_cart'),
    path('login', views.auth_login,name="login"),
    path('profile', views.profile,name="profile"),
    path('logout', views.logout_page,name="logout"),
  
] 