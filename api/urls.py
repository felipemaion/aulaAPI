from django.urls import path
from .views import *

urlpatterns = [
            path('aporte/<int:pk>', AporteDeleteUpdate.as_view()),
            path('aporte/', AporteView.as_view()),
]