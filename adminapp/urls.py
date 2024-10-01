from django.urls import path
from adminapp import views

urlpatterns = [
    path('index_page/',views.index_page,name="index_page"),
    path('add_category/',views.add_category,name="add_category"),
    path('save_category/',views.save_category,name="save_category"),
    path('display_category/',views.display_category,name="display_category"),
    path('edit_category/<int:cat_id>/',views.edit_category,name="edit_category"),
    path('edit_save/<int:cat_id>/', views.edit_save, name="edit_save"),
    path('delete_category/<int:cat_id>/', views. delete_category, name=" delete_category"),
    path('add_product/',views.add_product,name="add_product"),
    path('display_product/', views.display_product, name="display_product"),
    path('save_product/', views.save_product, name="save_product"),
    path('edit_product/<int:edit_id>/', views.edit_product, name="edit_product"),
    path('update_product/<int:edit_id>/', views.update_product, name="update_product"),
    path('delete_product/<int:edit_id>/', views.delete_product, name="delete_product"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_login_page/',views.admin_login_page,name="admin_login_page"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('contact_view/',views.contact_view,name="contact_view"),
    path('delete_message/<int:msg_id>/', views.delete_message, name="delete_message"),
    path('admin_view_user/',views.admin_view_user,name="admin_view_user")
]