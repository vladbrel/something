from django.contrib import admin

# Register your models here.

from .models import  Category, Product

class CategoryAdmin( admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category, CategoryAdmin) #связали эти две категории

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','available','created', 'update']
    list_filter = ['available','created', 'update']
    list_editable = ['price','stock','available']  #какие поля через админку сможем изменять
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Product, ProductAdmin)