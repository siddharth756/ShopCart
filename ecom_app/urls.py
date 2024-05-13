from django.urls import path
from .views import homeview,productview,filter_products,detailview,checkoutview,mobileview,tvview,electronicview,fashionview,beautyview,groceryview,furnitureview

app_name = "ecom_app"

urlpatterns = [
    path('',homeview,name="home"),
    path('products/',productview,name="products"),
    path('products/<int:pk>',detailview.as_view(),name="detail"),
    path('checkout/',checkoutview,name="checkout"),

    path('filter/<str:price_range>/', filter_products, name='filter_products'),

    path('mobiles/',mobileview,name="mobiles"),
    path('tvs/',tvview,name="tvs"),
    path('electronics/',electronicview,name="electronics"),
    path('fashion/',fashionview,name="fashion"),
    path('beauty/',beautyview,name="beauty"),
    path('grocery/',groceryview,name="grocery"),
    path('furniture/',furnitureview,name="furniture"),
]
