"""
perform tSNE analysis
"""

import pandas as pd
import numpy as np

#import sklearn
import sklearn
from sklearn import datasets, decomposition
from sklearn.manifold import TSNE

class performTSNE:
    
    def __init__(self):
        pass
            
    def tsne_descriptors(self, csv_name):
        """
        Input:
            csv_name : session csv_name
        Output:
            result: DataFrame whit tSNE result
        """
        numerated_libraries = pd.read_csv(f'generated_csv/{csv_name}', index_col= "Unnamed: 0")
        reference_libraries = pd.read_csv('modules/reference_libraries.csv', index_col= "Unnamed: 0")
        Data = pd.concat([numerated_libraries, reference_libraries], axis = 0)
        Data = Data.reset_index()
        _ = ["SMILES", "Sequence", "Library"]
        ref = Data[_]
        feature_names = ["HBA", "HBD", "RB", "LOGP","TPSA", "MW"] #configure manual if necessary
        model = TSNE(n_components=2,
                        init='pca',
                        random_state=1992, 
                        angle = 0.3,
                        perplexity=30
                        ).fit_transform(Data[feature_names])
        result = pd.DataFrame(data = model, columns=["PC 1","PC 2"])
        result = pd.concat([result, ref], axis = 1)
        return result, model

    def tsne_fingerprint(self, fp_matrix, ref):
        model = TSNE(n_components=2,
                        init='pca',
                        random_state=1992, 
                        angle = 0.3,
                        perplexity=30
                        ).fit_transform(fp_matrix)
        result = pd.DataFrame(data = model, columns=["PC 1","PC 2"])
        result = pd.concat([result, ref], axis = 1)
        return result, model