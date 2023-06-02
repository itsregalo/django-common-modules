from django.urls import path
from .views import UserFormView

urlpatterns = [
    path('', UserFormView.as_view(), name='user_form'),
]