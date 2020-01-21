from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from rest_framework.views import APIView

from .forms import InputForm
from Build.numerate import Numerate


class ServerViews(APIView):
    
    def post(self, request):
        form = InputForm(request.POST)
        form_dict = {
                        'form' : form,
                    }
        if form.is_valid():
            form = form.save()
            print(form.first)
            print(form.linear)
            print(form.methylated)
            print(form.topology)
            print(form.length)
            n = Numerate(form.first[0], form.linear, form.methylated, form.topology, form.length)
            n.write_databases()
            return HttpResponse("AMINOACIDOS SELECCIONADOS")
        return render(request,'form_page.html',context = form_dict)

    def get(self, request):
        form = InputForm()
        form_dict = {
                    'form' : form,
                    }
        return render(request,'form_page.html',context = form_dict)
