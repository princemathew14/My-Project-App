from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Project

class ProjectListView(ListView):
    model = Project
    template_name = 'myapp/project_list.html'
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'myapp/project_detail.html'

class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'description', 'start_date', 'end_date']
    template_name = 'myapp/project_form.html'
    success_url = reverse_lazy('myapp:project_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Project created successfully.')
        return response

class ProjectUpdateView(UpdateView):
    model = Project
    fields = ['name', 'description', 'start_date', 'end_date']
    template_name = 'myapp/project_form.html'
    success_url = reverse_lazy('myapp:project_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Project updated successfully.')
        return response

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'myapp/project_confirm_delete.html'
    success_url = reverse_lazy('myapp:project_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Project deleted successfully.')
        return super().delete(request, *args, **kwargs)

