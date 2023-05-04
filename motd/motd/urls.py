
from django.contrib import admin
from django.urls import path
from  mayonnaise import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("mayonnaise/<pk>",views.MayonnaiseList.as_view(), name="mayonnaise")
]
