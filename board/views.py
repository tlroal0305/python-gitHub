from django.shortcuts import render

# Create your views here.
def board(request):
  if request.method == "GET":
    context = {
      "title":"안녕 안녕",
      "content" : "연습으로 해보는"
    }
    return render (request, 'page/index.html', context=context)
  