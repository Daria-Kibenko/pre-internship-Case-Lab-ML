from django.urls import path
from .views import review_form, result

urlpatterns = [
    path('add_review/', review_form, name='add_review'),
    path('success/', result, name='success'),
]