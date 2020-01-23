from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

import os, glob, csv
import pandas as pd

from bokeh.embed import components

from rest_framework.views import APIView
from chemical_space.forms import Chem_space_form

from modules.chemical_space.pca import performPCA
from modules.chemical_space.tSNE import performTSNE
from modules.chemical_space.plot import Plot
from modules.fingerprint.compute_fingerprint import FP
# Create your views here.
class ChemicalSpaceView(APIView):
    
    def post(self, request):
        form = Chem_space_form(request.POST)
        csv_name = request.session['csv_name']  
        form_dict = {
                            'form' : form,
                        }
        if form.is_valid():
            form = form.save()
            if len(form.pca_fp) > 0: #PCA FINGERPRINT
                parameter = form.pca_fp[0]
                print(type(parameter), parameter)
                matrix_fp, ref = FP(csv_name, parameter).compute()
                #matrix_fp = pd.DataFrame(matrix_fp)
                result, model = performPCA().pca_fingerprint(matrix_fp, ref)
                plot = Plot(result).plot_pca(parameter)
                script, div = components(plot)
                return render_to_response('plot_pca.html', {'script': script, 'div': div})
            else:
                pass
            if len(form.tsne_fp) > 0: #TSNE FINGERPRINT
                parameter = form.tsne_fp[0]
                #print(type(parameter), parameter)
                matrix_fp, ref = FP(csv_name, parameter).compute()
                result, model = performTSNE().tsne_fingerprint(matrix_fp, ref)
                plot = Plot(result).plot_tsne(parameter)
                script, div = components(plot)
                return render_to_response('plot_pca.html', {'script': script, 'div': div})
            if len(form.pca_pp) > 0: #PCA DESCRIPTORS
                result, model = performPCA().pca_descriptors(csv_name)
                plot = Plot(result).plot_pca("physicochemical properties")
                script, div = components(plot)
                return render_to_response('plot_pca.html', {'script': script, 'div': div})
            else:
                pass
            if len(form.tsne_pp) > 0: #TSNE DESCRIPTORS
                print("form.tsne_pp", form.tsne_pp)
                result, model = performTSNE().tsne_descriptors(csv_name)
                print(result)
                plot = Plot(result).plot_tsne("physicochemical properties")
                script, div = components(plot)
                return render_to_response('plot_pca.html', {'script': script, 'div': div})
            else:
                pass
        #    return HttpResponse("You selected an option")
        else:
            print("no se por que no guarda cosas")
        return render(request,'chemical_space.html', context = form_dict)

    def get(self, request):
        form = Chem_space_form()
        #csv_name = request.session['csv_name']  
        form_dict = {
                            'form' : form,
                        }
        return render(request,'chemical_space.html', context = form_dict)