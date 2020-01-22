from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from rest_framework.views import APIView

import os, glob, csv
import pandas as pd
from datetime import datetime

from .forms import InputForm
from modules.build.numerate import Numerate


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
            DF = n.write_databases()
            print(DF.head())
            now = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f'database_{now}.csv'
            route = f'generated_csv/{filename}'
            request.session['csv_name'] = filename
            download_csv = DF.to_csv(route, encoding='utf-8', index = True)
            return redirect(f'/csv/{filename}/')
            #return HttpResponse("AMINOACIDOS SELECCIONADOS")
        return render(request,'form_page.html',context = form_dict)

    def get(self, request):
        form = InputForm()
        form_dict = {
                    'form' : form,
                    }
        return render(request,'form_page.html',context = form_dict)

class CSVView(APIView):
    def get(self, request, csv_name):
        data = pd.read_csv(f'generated_csv/{csv_name}')
        data_html = data.to_html()
        context = {'loaded_data': data_html}
        return render(request, 'table.html', context)


