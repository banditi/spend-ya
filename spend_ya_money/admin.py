from django.contrib import admin

from .models import Wallet


class YaMoneyAdmin(admin.ModelAdmin):
    list_display = ['created_at']

admin.site.register(Wallet, YaMoneyAdmin)
