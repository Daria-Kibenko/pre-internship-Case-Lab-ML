from django.contrib import admin
from django.urls import path
from reviews import views  # Импорт представлений из приложения reviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('review/', views.review_view, name='review'),  # Путь к форме отзыва
]