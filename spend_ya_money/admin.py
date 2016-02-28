from django.contrib import admin

from .models import YaMoney


class YaMoneyAdmin(admin.ModelAdmin):
    list_display = ['created_at']

admin.site.register(YaMoney, YaMoneyAdmin)
