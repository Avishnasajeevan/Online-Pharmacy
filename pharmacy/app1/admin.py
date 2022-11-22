from django.contrib import admin
from . models import  Brands, Category, Customer, Product, SubCategory,Cart

#table view in admin site
class AdminProduct(admin.ModelAdmin):
    list_display = ['pname', 'price','category', 'subcategory']   

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminSubCategory(admin.ModelAdmin):
    list_display = ['sname']

class AdminBrands(admin.ModelAdmin):
    list_display = ['bname']

class AdminCart(admin.ModelAdmin):
    list_display = ['user','product','product_qty']


# Register your models here.
admin.site.register(Product , AdminProduct)
admin.site.register(Category , AdminCategory)
admin.site.register(SubCategory , AdminSubCategory)
admin.site.register(Brands , AdminBrands)
admin.site.register(Customer),
admin.site.register(Cart, AdminCart)

