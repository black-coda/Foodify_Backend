from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


def test_view(request):
    return render(request, 'trial.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('main.urls')),
    path('', test_view, name='trial'),
]
