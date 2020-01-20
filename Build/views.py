from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from rest_framework.views import APIView

from Build.models import AminoAcid, First, Linear, Methylated
from Build.forms import InputForm, InputForm1, InputForm2, TopologyForm
# Create your views here.
from Build.amino_acid import dict_amino_acid
from Build.numerate import Numerate


class ServerViews(APIView):
    
    def post(self, request):
        form = InputForm(request.POST)
        form1 = InputForm1(request.POST)
        form2 = InputForm2(request.POST)
        form3 = TopologyForm(request.POST)
        date_dict = {
                    'form' : form,
                    'form1': form1,
                    "form2": form2,
                    "form3": form3,
                    }
        if form.is_valid() and form1.is_valid() and form2.is_valid():
            #form = form.save(commit=False)
            first = form.cleaned_data["first"]
            print(first)
            form1 = form1.save(commit=False)
            form1.save()
            form2 = form2.save(commit=False)         
            form2.save()
            form3 = form3.save(commit=False)         
            form3.save()
            n = Numerate(first[0], form1.linear, form2.methylated, form3.topology, form3.length)
            n.write_databases()#print(form.first)
            return HttpResponse("AMINOACIDOS SELECCIONADOS")
        elif form.is_valid() and form1.is_valid():
            form = form.save(commit=False)
            form.save()
            form1 = form1.save(commit=False)
            form1.save()
            form2 = []
            form3 = form3.save(commit=False)         
            form3.save()
            n = Numerate(first, form1.linear, form2, form3.topology, form3.length)
            n.write_databases()#print(form.first)
            return HttpResponse("AMINOACIDOS SELECCIONADOS")
            #return HttpResponse("AMINOACIDOS SELECCIONADOS")
        elif form.is_valid() and form2.is_valid():
            form = form.save(commit=False)
            form.save()
            form1 = []
            form2 = form2.save(commit=False)
            form2.save()
            n = Numerate(form.first, form1, form2.methylated)
                    
            return HttpResponse("AMINOACIDOS SELECCIONADOS")
        return render(request,'home_page.html',context = date_dict)

    def get(self, request):
        form = InputForm()
        form1 = InputForm1()
        form2 = InputForm2()
        form3 = TopologyForm()
        date_dict = {
                    'form' : form,
                    'form1': form1,
                    "form2": form2,
                    "form3": form3,
                    }
        return render(request,'home_page.html',context = date_dict)
    
class DropViews(APIView):
    
    def post(self, request):
        form = InputForm(request.POST)
        form1 = InputForm1(request.POST)
        form2 = InputForm2(request.POST)
        form3 = TopologyForm(request.POST)
        date_dict = {
                    'form' : form,
                    'form1': form1,
                    "form2": form2,
                    "form3": form3,
                    }
        if form.is_valid() and form1.is_valid() and form2.is_valid():
            #form = form.save(commit=False)
            first = form.cleaned_data["first"]
            print(first)
            form1 = form1.cleaned_data["linear"]
            print(form1)
            form2 = form2.save(commit=False)         
            form2.save()
            form3 = form3.save(commit=False)         
            form3.save()
            n = Numerate(first, form1, form2.methylated, form3.topology, form3.length)
            n.write_databases()#print(form.first)
            return HttpResponse("AMINOACIDOS SELECCIONADOS")
        elif form.is_valid() and form1.is_valid():
            form = form.save(commit=False)
            form.save()
            form1 = form1.save(commit=False)
            form1.save()
            form2 = []
            form3 = form3.save(commit=False)         
            form3.save()
            n = Numerate(first, form1.linear, form2, form3.topology, form3.length)
            n.write_databases()#print(form.first)
            return HttpResponse("AMINOACIDOS SELECCIONADOS")
            #return HttpResponse("AMINOACIDOS SELECCIONADOS")
        elif form.is_valid() and form2.is_valid():
            form = form.save(commit=False)
            form.save()
            form1 = []
            form2 = form2.save(commit=False)
            form2.save()
            n = Numerate(form.first, form1, form2.methylated)
                    
            return HttpResponse("AMINOACIDOS SELECCIONADOS")
        return render(request,'drop.html',context = date_dict)

    def get(self, request):
        form = InputForm()
        form1 = InputForm1()
        form2 = InputForm2()
        form3 = TopologyForm()
        date_dict = {
                    'form' : form,
                    'form1': form1,
                    "form2": form2,
                    "form3": form3,
                    }
        return render(request,'drop.html',context = date_dict)
