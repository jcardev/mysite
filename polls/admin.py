from django.contrib import admin

from .models import Choice, Question
# permite que las encuestas se puedan modificar en el sitio
"""" parte 7 se incluye la clase para personalizar el orden de los campos
 y se pasa como parametor al register de la clase admin.
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
"""
""" dividir el formulario en grupos pequeños.
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
"""

#permite agregar hasta 3 respuestas por pregunta
#class ChoiceInline(admin.StackedInline):
# se cambia linea para mostrarlo de forma tabular y evitar que ocupe mucho espacio en pantalla
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    #mostrar los campos como columnas
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    #incluye filtro de fecha
    list_filter = ['pub_date']
    #permitir buscar por texto de fecha, se pueden incluir varios, pero no muchos ya que la petición es like
    search_fields = ['question_text']



admin.site.register(Question, QuestionAdmin)
# registro que permite ingresar una respuesta por pregunta, lo que es inefisciente
#admin.site.register(Choice)

