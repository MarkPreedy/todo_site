from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='todo'),
    path('remove/<int:item_id>/', views.remove, name='remove'),
    path('update/<int:item_id>/', views.index, name='update'),  # Reuse the index view for updates
]