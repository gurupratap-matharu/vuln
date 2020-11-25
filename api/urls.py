from django.urls import path

from api.views import DatasetAPIView

urlpatterns = [
    path('', DatasetAPIView.as_view()),
]
