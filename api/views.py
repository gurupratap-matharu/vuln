from datasets.models import Dataset
from datasets.serializers import DatasetSerializer
from rest_framework import generics


class DatasetAPIView(generics.ListAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer
