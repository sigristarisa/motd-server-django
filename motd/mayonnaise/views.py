from django.shortcuts import render

# Create your views here.
def mayonnaise(request):
    context = {id: 1}
    return render(request, "mayonnaise/mayonnaise.html", context)