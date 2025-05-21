from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Project
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-id')
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'myapp/project_list.html'
    context_object_name = 'projects'

class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'myapp/project_detail.html'  # Optional if using default
    context_object_name = 'project'              # Optional: makes template cleaner


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['name', 'description', 'start_date', 'end_date']
    template_name = 'myapp/project_form.html'
    success_url = reverse_lazy('myapp:project_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, 'Project created successfully.')
        return super().form_valid(form)



class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['name', 'description', 'start_date', 'end_date']
    template_name = 'myapp/project_form.html'
    success_url = reverse_lazy('myapp:project_list')

    def form_valid(self, form):
        messages.success(self.request, 'Project updated successfully.')
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff or self.get_object().owner == self.request.user


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = 'myapp/project_confirm_delete.html'
    success_url = reverse_lazy('myapp:project_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Project deleted successfully.')
        return super().delete(request, *args, **kwargs)

    def test_func(self):
        return self.request.user.is_staff or self.get_object().owner == self.request.user

