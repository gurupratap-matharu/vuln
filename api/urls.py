from datasets.admin import DatasetAdmin
from django.urls import path

from api.views import DatasetAPIView

urlpatterns = [
    path('', DatasetAdmin.as_view()),
]
