import pandas as pd

data = pd.read_csv('modules/reference_libraries.csv', index_col= "Unnamed: 0")
#print(data.head())

"""Compute Fingerprint"""
import numpy as np
import pandas as pd

import rdkit    
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem, MACCSkeys
from rdkit.Chem.Fingerprints import FingerprintMols
from rdkit.Chem.AtomPairs import Pairs  


class FP:

    def __init__(self, data):
        self.data = data

    def fp_matrix(self, fp):
        output = []
        for f in fp:
            arr = np.zeros((1,))
            DataStructs.ConvertToNumpyArray(f, arr)
            output.append(arr)
        matrix_fp = np.asarray(output)
        return matrix_fp

    def maccskeys_fp(self):
        ms=[Chem.MolFromSmiles(i) for i in self.data.SMILES]
        fp = [MACCSkeys.GenMACCSKeys(x) for x in ms]
        return fp

    def ecfp4_fp(self):
        ms = [Chem.MolFromSmiles(i) for i in self.data.SMILES]
        fp = [AllChem.GetMorganFingerprintAsBitVect(x,2) for x in ms]
        return fp

    def ecfp6_fp(self):
        ms=[Chem.MolFromSmiles(i) for i in self.data.SMILES]
        fp = [AllChem.GetMorganFingerprintAsBitVect(x,3) for x in ms]
        return fp

    def compute(self):
        ref = self.ref
        if self.parameter == "MACCS Keys":
            fp = self.maccskeys_fp()
            matrix_fp = self.fp_matrix(fp)
            return matrix_fp, ref
        elif self.parameter == "ECFP 4":
            fp = self.ecfp4_fp()
            matrix_fp = self.fp_matrix(fp)
            return matrix_fp, ref
        elif self.parameter == "ECFP 6":
            fp = self.ecfp6_fp()
            matrix_fp = self.fp_matrix(fp)
            return matrix_fp, ref
        elif self.parameter == "Topological":
            fp = self.topological_fp()
            matrix_fp = self.fp_matrix(fp)
            return matrix_fp, ref
        elif self.parameter == "Atom Pair":
            fp = self.atom_pair_fp()
            matrix_fp = self.fp_matrix(fp)
            return matrix_fp, ref
        else:
            return ("Not allow")
        #else:
        #    pass
        #return matrix_fp, ref

d  = FP(data).ecfp6_fp()
print("ya calcule fp")
matrix = FP(data).fp_matrix(d)
print("ya calcule la matriz")
df = pd.DataFrame(data = matrix)
df["Sequence"] = data["Sequence"].to_list()#ref = data[_].reset_index()
df["Library"] = data["Library"].to_list()
print(df.head())
df.to_csv("modules/reference_libraries_ECFP6.csv")