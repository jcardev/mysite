from django.urls import path
from . import views
""" La función path() recibe 4 argumentos, dos requeridos route y view
    y dos opcionales kwargs y name.
    route: es una cadena que contiene un patrón de URL. cuando django recibe una peticiòn
    comienza por el primer patrón y continua hacia abajo por la lista
    view: cuando django encuentra una coincidencia de expresiones regulares llama a la funciòn 
    de la vista especificada con un objeto httpRequest como primer argumento y cualquiera
    de los valores capturados de la rita como argumentos de palabra clave
    kwargs: los argumentos arbitrarios de palabra clave se pueden pasar en un diccionario
    de la vista destino.
    name: dar nombre único a la url, permite cambiar 
    """
app_name ='polls'
urlpatterns = [path('', views.index, name='index'),
               path('<int:question_id>/', views.detail, name='detail'),
               path('<int:question_id>/results/', views.results, name='results'),
               path('<int:question_id>/vote/', views.vote, name='vote'),
               ]
