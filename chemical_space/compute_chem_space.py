import pandas as pd

from modules.chemical_space.pca import PCA
from modules.chemical_space.plot import Plot

class PlotChemSpace:

    def __init__(self, csv_name, selected_plot):
        self.csv_name = csv_name
        self.generated_csv = pd.read_csv(f'generated_csv/{csv_name}')
        self.selected_plot = selected_plot

    def pca_fp(self):
        print(self.selected_plot)
        result = ["result pca_fp"]

        return result
    
    def tsne_fp(self):
        print(self.selected_plot)
        result = ["result pca_fp"]
        return result
    
    #def pca_pp(self):
    #    pca = PCA(self.csv_name)
    #    result, model = pca.pca_descriptors()

    def tsne_pp(self):
        print(self.selected_plot)
        result = ["result pca_fp"]
        return result

    #def plot_pca(self, result):
    #    print("voy a hacer un grafico de pca")
    #    return "voy a hacer el grafico"
    
    def plot_tsne(self, result):
        print("voy a hacer un grafico de tsne")
        return "voy a hacer el grafico"
