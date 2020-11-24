from django.urls import path

from datasets.views import DatasetListView

urlpatterns = [
    path('', DatasetListView.as_view(), name='home'),
]
