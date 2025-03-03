from django.urls import path
from ranking.views import ranking, inicio, agregar_jugador, ver_jugador, about, ModificarJugadorView, EliminarJugadorView

urlpatterns = [
    path('', inicio, name="inicio"),
    path('ranking/', ranking, name="ranking"),
    path('agregar-jugador/', agregar_jugador, name="agregar_jugador"),
    path('ver-jugador/<int:jugador_id>/', ver_jugador, name="ver_jugador"),
    path('about/', about, name="about"),
    # Vistas comunes
    # path('eliminar-jugador/<int:jugador_id>/', eliminar_jugador, name="eliminar_jugador"),
    # path('modificar-jugador/<int:jugador_id>', modificar_jugador, name="modificar_jugador"),
    # CBV
    path('eliminar-jugador/<int:pk>/', EliminarJugadorView.as_view(), name="eliminar_jugador"),
    path('modificar-jugador/<int:pk>/', ModificarJugadorView.as_view(), name="modificar_jugador"),
]