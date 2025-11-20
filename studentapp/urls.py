from django.urls import path
from studentapp.views import *

urlpatterns = [

    path('home/', home_view, name='home'),
    path('display/', display_view, name='display'),
    path('insert/', insert_view, name='insert'),
    path('update/<int:id>/', update_view, name='update'),
    path('delete/<int:id>/', delete_view, name='delete'),
    
]
    
