from django.shortcuts import render
from django.views.generic import ListView
from .models import Mayonnaise

class MayonnaiseList(ListView):
    model = Mayonnaise

    def get_mayonnaise_by_id(self):
        return Mayonnaise.objects.get(pk=self.id)