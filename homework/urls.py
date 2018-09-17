from django.contrib import admin
from django.urls import path
from homework.app.views import page, pages, category, unknown_category

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', page),
    path('<int:id>/', page),
    path('pages/', pages),
    path('category/<int:id>', category),
    path('category/unknown', unknown_category),
]
