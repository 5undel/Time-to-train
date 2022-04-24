from django.contrib import admin
from .models import CreateMembership , MembershipNumber
# Register your models here.

# Creating readonly 
class MembershipLineItemAdminInLine(admin.TabularInline):
    model = MembershipNumber
    readonly_fields = ('linitem_total',)


class MembershipAdmin(admin.ModelAdmin):
    inlines = (MembershipLineItemAdminInLine,)

    readonly_fields = ('membership_number', 'start_date',
                       'grand_total', 'order_total',)
    
    fields = ('membership_number', 'membership_typ', 'start_date',
              'full_name', 'email', 'phone_number', 
              'country', 'town_or_city', 'street_address1', 
              'street_address2', 'order_total',
              'grand_total', )

    list_display = ('full_name', 'start_date', 'order_total', 
                    'membership_number',)
    
    ordering = ('full_name',)

admin.site.register(CreateMembership, MembershipAdmin)
admin.site.register(MembershipNumber)