from django.contrib import admin
from .models import Project, User, Task, Comment, TimeLog

admin.site.register(Project)
admin.site.register(User)
admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(TimeLog)
