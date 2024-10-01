from django.urls import path
from webapp import views

urlpatterns = [
    path('home_page/',views.home_page,name="home_page"),
    path('about_us/',views.about_us,name="about_us"),
    path('contact_page/',views.contact_page,name="contact_page"),
    path('save_message/',views.save_message,name="save_message"),
    path('products_page/',views.products_page,name="products_page"),
    path('single_product/<int:pro_id>/',views.single_product,name="single_product"),
    path('filtered_product/<cat_name>/',views.filtered_product,name="filtered_product"),
    path('signup/',views.signup,name="signup"),
    path('save_signup/',views.save_signup,name="save_signup"),
    path('reg_login/',views.reg_login,name="reg_login"),
    path('',views.user_login,name="user_login"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('cart_page/',views.cart_page,name="cart_page"),
    path('delete_cart/<int:cart_id>/',views.delete_cart,name="delete_cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('payment_page/',views.payment_page,name="payment_page"),
    path('checkout_save/',views.checkout_save,name="checkout_save")
]
