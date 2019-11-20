from django.contrib import admin

# Register your models here.
from .models import Product, Contact, Orders, OrderUpdate, Newsletter

class ProductAdmin(admin.ModelAdmin):
	  list_display = ['product_name','category','price']
	  search_fields = ['product_name','category','price']
	  list_filter = ['product_name','category','price']



admin.site.register(Product, ProductAdmin)

class ContactAdmin(admin.ModelAdmin):
	  list_display = ['name','email','phone']
	  search_fields = ['name','email','phone']
	  list_filter = ['name','email','phone']



admin.site.register(Contact, ContactAdmin)

class OrdersAdmin(admin.ModelAdmin):
	  list_display = ['name','amount','city']
	  search_fields = ['name','amount','city']
	  list_filter = ['name','amount','city']



admin.site.register(Orders, OrdersAdmin)

class OrderUpdateAdmin(admin.ModelAdmin):
	  list_display = ['order_id','update_desc','timestamp']
	  search_fields = ['order_id','update_desc','timestamp']
	  list_filter = ['order_id','update_desc','timestamp']



admin.site.register(OrderUpdate, OrderUpdateAdmin)

class NewsletterAdmin(admin.ModelAdmin):
	  list_display = ['name','email','phone']
	  search_fields = ['name','email','phone']
	  list_filter = ['name','email','phone']



admin.site.register(Newsletter, NewsletterAdmin)