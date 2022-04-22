from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'important', 'created', 'datecompleted')
    list_filter = ('important', 'created', 'datecompleted')
    search_fields = ('title', 'memo')
    list_editable = ('important',)
    readonly_fields = ('created',)


admin.site.register(Todo, TodoAdmin)