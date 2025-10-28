from django.contrib import admin
from .models import CallLog

@admin.register(CallLog)
class CallLogAdmin(admin.ModelAdmin):
    list_display = ('caller_name', 'phone_number', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('caller_name', 'phone_number')

