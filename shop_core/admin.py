from django.contrib import admin
from .models import *

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

@admin.register(Product)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [ PropertyImageInline, ]

admin.site.register(Menu)
admin.site.register(Category)
admin.site.register(ModelPhone)
admin.site.register(Card)
admin.site.register(CartItem)