from django.contrib import admin

from .models import User, EntityRequest, IndividualRequest, Payment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_full_name', 'email']


@admin.register(IndividualRequest)
class IndividualRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'birth_day',
                    'region', 'city']
    list_filter = ['region', 'city']


@admin.register(EntityRequest)
class EntityRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'address', 'phone_number']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass
