from django.contrib import admin
from .models import NewOrder, OrderProduct


class ItemInline(admin.StackedInline):
    model = OrderProduct


class NewOrderAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
    list_display = ['first_name', 'email', 'data_created', 'status']
    list_filter = ['data_created', 'status']


admin.site.register(NewOrder, NewOrderAdmin)
