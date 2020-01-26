"""Compute Fingerprint"""
import numpy as np
import pandas as pd

import rdkit    
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem, MACCSkeys
from rdkit.Chem.Fingerprints import FingerprintMols
from rdkit.Chem.AtomPairs import Pairs  

class FP:

    def __init__(self, csv_name, fp_name):
        self.fp_name = fp_name
        self.Data = pd.read_csv(f'generated_csv/{csv_name}', index_col= "Unnamed: 0")
        _ = ["Sequence", "Library"]
        self.ref = self.Data[_].as_matrix()
        
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
        fp = [Pairs.GetAtomPairFingerprintAsIntVect(x) for x in ms]
        return fp

    def compute(self):
        ref = self.ref
        if self.fp_name == "MACCS Keys":
            fp = self.maccskeys_fp()
            matrix_fp = self.fp_matrix(fp)
            return matrix_fp, ref
        elif self.fp_name == "ECFP 4":
            fp = self.ecfp4_fp()
            matrix_fp = self.fp_matrix(fp)
            return matrix_fp, ref
        elif self.fp_name == "ECFP 6":
            fp = self.ecfp6_fp()
            matrix_fp = self.fp_matrix(fp)
            return matrix_fp, ref
        elif self.fp_name == "Topological":
            fp = self.topological_fp()
            matrix_fp = self.fp_matrix(fp)
            return matrix_fp, ref
        elif self.fp_name == "Atom Pair":
            fp = self.atom_pair_fp()
            matrix_fp = self.fp_matrix(fp)
            return matrix_fp, ref
        else:
            return ("Not allow")
