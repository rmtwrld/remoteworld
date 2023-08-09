from django.contrib import admin
from .models import Location, Space

@admin.register(Location, Space)
class WorkspaceAdmin(admin.ModelAdmin):
    pass
