from django.contrib import admin
from owner.models import*
# Register your models here.

admin.site.register(Categories)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Carts)
admin.site.register(Reviews)