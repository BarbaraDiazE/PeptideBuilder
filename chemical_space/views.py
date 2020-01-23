from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from bokeh.embed import components

from rest_framework.views import APIView

import os, glob, csv

from chemical_space.forms import Chem_space_form
#from chemical_space.compute_chem_space import PlotChemSpace

from modules.chemical_space.pca import PCA
from modules.chemical_space.plot import Plot

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
            if len(form.pca_fp) > 0:
                #plot = PlotChemSpace(csv_name, form.pca_fp)
                #result = plot.pca_fp()
                #plot.plot_pca(result)
                pass
            else:
                pass
            if len(form.tsne_fp) > 0:
                # = PlotChemSpace(csv_name, form.tsne_fp)
                #result = plot.tsne_fp()
                #plot.plot_tsne(result)
                pass
            else:
                pass
            if len(form.pca_pp) > 0:
                pca = PCA(csv_name)
                result, model = pca.pca_descriptors()
                plot = Plot(result).plot_pca()
                script, div = components(plot)
                return render_to_response('plot_pca.html', {'script': script, 'div': div})
            else:
                pass
            if len(form.tsne_pp) > 0:
                #plot = PlotChemSpace(csv_name, form.tsne_pp)
                #result = plot.tsne_pp()
                #plot.plot_tsne(result)
                pass
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