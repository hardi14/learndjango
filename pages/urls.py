from django.contrib import admin
from django.urls import path 
from .views import HomeView, AboutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="homepage"),
    path('about/', AboutView.as_view(), name="about.html")

]