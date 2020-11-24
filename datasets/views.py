from django.views.generic import ListView

from datasets.models import Dataset


class DatasetListView(ListView):
    model = Dataset
    context_object_name = 'dataset_list'
    paginate_by = 20
    template_name = 'datasets/dataset_list.html'
