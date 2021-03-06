from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from core.models import Vacancy

class IndexView(TemplateView):
	template_name = 'core/index.html'

class VacancyListView(ListView):
    model = Vacancy

class VacancyCreateView(CreateView):
    model = Vacancy
    template_name = 'core/vacancy_create.html'
    fields = '__all__'
    success_url = reverse_lazy('vacancy_list')

class VacancyDetailView(DetailView):
    model = Vacancy

class VacancyUpdateView(UpdateView):
    model = Vacancy
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('vacancy_list')

class VacancyDeleteView(DeleteView):
    model = Vacancy
    success_url = reverse_lazy('vacancy_list')