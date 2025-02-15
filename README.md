# 📊 Ranking de Jugadores

Aplicación web desarrollada en Django para gestionar y visualizar un ranking de jugadores con estadísticas como puntos, participaciones y promedio.
Ademas se podrá hacer seguimiento de los distintos torneos que se van realizando durante la temporada.

## 🚀 Tecnologías Usadas
- Django

## 🔧 Instalación

1. **Clonar el repositorio:**
   Desde Git Bash:
   git clone https://github.com/RomanoDan/Proyecto_AJUPAM.git
   
2. **Crear y configurar el entorno virtual:**
    Posicionados en la carpeta del proyecto:
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate

3. **Iniciar el servidor y acceder a la web local:**
    python manage.py runserver
    Accede desde el navegador a http://127.0.0.1:8000/

## 🛠️ Funcionalidades

En el inicio de la web, tendrás la opción de navegar por las opciones disponibles de la web.

**Listado de Jugadores**
    En este apartado se podrá visualizar los jugadores cargados en la base de datos y filtrar la busqueda por nombre o categoria.
**Agregar Jugador**
    En este apartado se podrá realizar la carga de un Jugador nuevo a la base de datos con sus correspondientes datos.