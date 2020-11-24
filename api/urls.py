from django.urls import path

from api.views import DataAPIView

urlpatterns = [
    path('', DataAPIView.as_view()),
    path('train/'),
    path('dataset/',),
    path('evaluate/',),
]
