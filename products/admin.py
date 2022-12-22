from django.contrib import admin
from .models import Product,ProductImages,Brand,Category,ProductReview
# Register your models here.

class ProductImageTabular(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageTabular]
    list_display = ['name','price','flag','quantity']
    list_filter = ['flag','brand','category','price']
    search_fields = ['name','desc','subtitle']


admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(ProductReview)