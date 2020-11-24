from django.contrib import admin

from datasets.models import Dataset


class DatasetAdmin(admin.ModelAdmin):
    list_display = ('title', 'dataset', 'created_on')
    list_filter = ('created_on',)


admin.site.register(Dataset, DatasetAdmin)
