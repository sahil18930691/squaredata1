from django.urls import path
from .views import GetData
from django.conf import settings
from django.conf.urls.static import static

app_name = 'api_data'

urlpatterns = [
    # Payment Statuses
    path('', GetData.as_view(), name='get_data'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)