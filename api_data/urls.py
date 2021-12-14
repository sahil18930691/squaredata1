from django.urls import path
from .views import GetData


app_name = 'api_data'

urlpatterns = [
    # Payment Statuses
    path('', GetData.as_view(), name='get_data'),
]