"""
perform tSNE
"""

import pandas as pd
import numpy as np

#import sklearn
import sklearn
from sklearn import datasets, decomposition
from sklearn.manifold import TSNE

class TSNE:

    def __init__(self, fp_matrix, ref):
        self.fp_matrix = fp_matrix
        self.ref = ref

    def pca_fingerprint(self):
        # Perform the tSNE
        model = TSNE(n_components=2,
                        init='pca',
                        random_state=1992, 
                        angle = 0.3,
                        perplexity=30
                        ).fit_transform(self.fp_matrix)
        result = pd.DataFrame(data = model, 
                                columns=["PC 1","PC 2"]
                                )

        result = pd.concat([pca_result, self.ref_DF], axis = 1)
        #variance = list(model.explained_variance_ratio_)
        print(result.Library.unique())
        #self.a = round(variance[0] * 100, 2)
        #self.b = round(variance[1] * 100, 2)
        return result, model