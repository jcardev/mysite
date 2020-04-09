from django.contrib import admin

from .models import Question
# permite que las encuestas se puedan modificar en el sitio
admin.site.register(Question) 