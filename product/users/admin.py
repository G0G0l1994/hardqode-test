from django.contrib import admin
from users.models import CustomUser, Balance, Subscription


@admin.register(CustomUser)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['username','email']


@admin.register(Subscription)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['user','course','active',]
    


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ['user_balance','value']

