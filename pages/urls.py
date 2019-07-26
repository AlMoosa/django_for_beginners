from django.urls import path
from .views import HomePageView, AboutPageView


urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]

# При использовании представлений на основе классов
#  вы всегда добавляете as_view()в конце имени представления.