from django.contrib import admin
from .models import Product,Order,Category,TopProduct
from django.utils.html import format_html

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','image_url','page_url']

class TopProductAdmin(admin.ModelAdmin):
    fields = ['category','pid','name','price','description','image','image_url']
    list_display = ['pid','category','image_display','name','price']
    def image_display(self, obj):
        return format_html('<img src="{}" style="width: 25px;" />', obj.image_url)

    image_display.short_description = 'Image' 

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','image_display','name','price','category']
    search_fields = ['name','category']
    list_filter = ['category']
    list_editable = ['category']
    fields = ['category','name','price','description','image','image_url']

    def image_display(self, obj):
        return format_html('<img src="{}" style="width: 25px;" />', obj.image_url)

    image_display.short_description = 'Image' 

class OrderAdmin(admin.ModelAdmin):
    list_display = ['name','total','items','email','address','address2','city','state','zipcode']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(TopProduct,TopProductAdmin)

admin.site.site_title="ShopCart"
admin.site.site_header="ShopCart | E-commerce Site"
admin.site.index_title="Manage Shoppings"