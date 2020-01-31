"""Compute Fingerprint"""
import numpy as np
import pandas as pd
import itertools as it

import rdkit    
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem, MACCSkeys
from rdkit.Chem.Fingerprints import FingerprintMols
from rdkit.Chem.AtomPairs import Pairs  

class FP:

    def __init__(self, csv_name, fp_name):
        self.fp_name = fp_name[0]
        self.Data = pd.read_csv(f'generated_csv/{csv_name}', index_col= "Unnamed: 0")
        if self.Data.shape[0] > 1001:
            self.Data = self.Data.sample(500, replace=True, random_state=1992)
        else:
            self.Data = self.Data
        _ = ["Sequence", "Library"]
        self.ref = self.Data[_].as_matrix()
        self.diccionario = {
                            "MACCS Keys": self.maccskeys_fp(),
                            "ECFP 4": self.ecfp4_fp(),
                            "ECFP 6": self.ecfp6_fp() ,
                            "Topological": self.topological_fp(),
                            "Atom Pair": self.atom_pair_fp(),
                                    }
    
    def fp_matrix(self, fp):
        matrix_fp = []
        for f in fp:
            arr = np.zeros((1,))
            DataStructs.ConvertToNumpyArray(f, arr)
            matrix_fp.append(arr)
        return matrix_fp

    def maccskeys_fp(self):
        ms=[Chem.MolFromSmiles(i) for i in self.Data.SMILES]
        fp = [MACCSkeys.GenMACCSKeys(x) for x in ms]
        return fp

    def ecfp4_fp(self):
        ms = [Chem.MolFromSmiles(i) for i in self.Data.SMILES]
        fp = [AllChem.GetMorganFingerprintAsBitVect(x,2) for x in ms]
        return fp

    def ecfp6_fp(self):
        ms=[Chem.MolFromSmiles(i) for i in self.Data.SMILES]
        fp = [AllChem.GetMorganFingerprintAsBitVect(x,3) for x in ms]
        return fp

    def topological_fp(self):
        ms =[Chem.MolFromSmiles(i) for i in self.Data.SMILES]
        fp = [FingerprintMols.FingerprintMol(x) for x in ms]
        return fp

    def atom_pair_fp(self):
        ms = [Chem.MolFromSmiles(i) for i in self.Data.SMILES]
        fp = [Pairs.GetAtomPairFingerprintAsBitVect(x) for x in ms]
        return fp

    def compute_asmatrix(self):
        ref = self.ref
        fp = self.diccionario[self.fp_name]
        matrix_fp = self.fp_matrix(fp)
        return matrix_fp, ref
    
    def compute_similarity(self, df_fp, library):
        fp = df_fp[df_fp["Library"]==library].fp
        sim = [DataStructs.FingerprintSimilarity(y,x) for x,y in it.combinations(fp, 2)]
        sim = [ round(_, 2) for _ in sim ]
        sim.sort()
        sim = np.asarray(sim) 
        y = np.arange(1, len(sim) + 1)/ len(sim) #eje y
        return sim, y

    def similarity(self, fp_name):
        fp_name = fp_name[0].replace(' ', '')
        fp = self.diccionario[self.fp_name]
        df_fp = pd.DataFrame.from_dict({ "fp" : fp, "Library": self.Data.Library})
        sim_linear, y_linear = self.compute_similarity(df_fp, "linear")
        sim_cyclic, y_cyclic = self.compute_similarity(df_fp, "cyclic")
        lib_linear  = np.asarray(["linear" for i in range(len(sim_linear))])
        lib_cyclic = np.asarray(["cyclic" for i in range(len(sim_cyclic))])
        pep_result = {
                        "sim": np.concatenate((sim_linear, sim_cyclic), axis = 0),
                        "y": np.concatenate((y_linear, y_cyclic), axis = 0),
                        "Library": np.concatenate((lib_linear, lib_cyclic), axis = 0)
                    }
        pep_result = pd.DataFrame.from_dict(pep_result)
        ref_data = pd.read_csv(f'modules/similatiry_reference_libraries_{fp_name}.csv', index_col= "Unnamed: 0")
        #ref_data = ref_data.sample(frac=0.1, replace=True, random_state=1992)
        result = pd.concat([pep_result, ref_data], axis = 0)
        return result
        
