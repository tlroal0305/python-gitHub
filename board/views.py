from django.shortcuts import render

# Create your views here.
def board(request):
  if request.method == "GET":
    return render (request, 'index.html')
  