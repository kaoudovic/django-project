from django.urls import path
from .views import form_company,insert,delete,update,backend_up,index
urlpatterns = [
    path('form/', form_company, name='form'),
    path('insert/', insert, name='insert'),
    path('delete/<int:id>', delete, name='delete'),
    path('update/<int:id>/', update, name='update'),
    path('backend_up/<int:id>', backend_up, name='backend_up'),
]