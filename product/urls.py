from django.urls import path
from . import views

urlpatterns = [
    path('add_product',views.add_product, name='add_product'),
    path('view_product',views.view_product, name='view_product'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]
