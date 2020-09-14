from django.contrib import admin
from .models import Todo

# to display some fields as a read only
class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Todo, TodoAdmin)
