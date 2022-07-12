from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Direction

# Create your views here.

class HomePageView(View):
    def get(self, request):
        directions = Direction.objects.all()
        context = {'directions':directions}
        return render(request, "index.html", context)


def change_lang(request):
    lang = request.GET.get('current_lang')
    if lang in ['uz','ru','en']:
        request.session['lang'] = lang
    return JsonResponse({"status":200})
