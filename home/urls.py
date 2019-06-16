from django.conf.urls import url, include
from .views import index_home_function

urlpatterns = [
    url(r'^$', index_home_function, name='home'),
]