from django.contrib import admin
from .models import Product,Orders,OrderUpdate

#from.models import OrderItem
class OrderUpdateAdmin(admin.ModelAdmin):
    list_display = ('update_id',
    'order_id',
    'update_desc',
    'timestamp'   )
    list_editable = ['update_desc']
    list_filter = ['timestamp']


admin.site.register(Product)
admin.site.register(OrderUpdate, OrderUpdateAdmin)
#admin.site.register(Orders)
#admin.site.register(Address)
#admin.site.register(Payment)

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order_id',
                    'items_json', 'name', 'email','address', 'city',
                    'state','zip_code', 'phone', 'amount')

    list_editable = ['amount']
    list_filter = ['order_id']

admin.site.register(Orders,OrdersAdmin)