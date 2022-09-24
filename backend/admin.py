from django.contrib import admin

from .models import User, EntityRequest, IndividualRequest, Payment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_full_name', 'phone_number', 'date_joined']


@admin.register(IndividualRequest)
class IndividualRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone_number',
                    'region', 'city', 'paid']
    list_filter = ['region', 'city']


@admin.register(EntityRequest)
class EntityRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'address', 'phone_number', 'paid']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'transaction_id']
