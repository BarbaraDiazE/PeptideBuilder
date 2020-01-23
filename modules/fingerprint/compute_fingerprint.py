"""Compute Fingerprint"""
import numpy as np
import pandas as pd

import rdkit    
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem, MACCSkeys
from rdkit.Chem.Fingerprints import FingerprintMols
from rdkit.Chem.AtomPairs import Pairs  


class FP:

    def __init__(self, csv_name, parameter):
        self.parameter = parameter
        numerated_libraries = pd.read_csv(f'generated_csv/{csv_name}', index_col= "Unnamed: 0")
        reference_libraries = pd.read_csv('modules/reference_libraries.csv', index_col= "Unnamed: 0")
        #reference_libraries = pd.read_csv(f'modules/databases/reference_libraries_{parameter}.csv', index_col= "Unnamed: 0")
        Data = pd.concat([numerated_libraries, reference_libraries], axis = 0)
        Data = Data.reset_index()
        self.smiles = Data.SMILES
        _ = ["Sequence", "Library"]
        self.ref = Data[_]

    def fp_matrix(self, fp):
        output = []
        for f in fp:
            arr = np.zeros((1,))
            DataStructs.ConvertToNumpyArray(f, arr)
            output.append(arr)
        matrix_fp = np.asarray(output)
        return matrix_fp

    def maccskeys_fp(self):
        ms=[Chem.MolFromSmiles(i) for i in self.smiles]
        fp = [MACCSkeys.GenMACCSKeys(x) for x in ms]
        return fp

    def ecfp4_fp(self):
        ms = [Chem.MolFromSmiles(i) for i in self.smiles]
        fp = [AllChem.GetMorganFingerprintAsBitVect(x,2) for x in ms]
        return fp

    def ecfp6_fp(self):
        ms=[Chem.MolFromSmiles(i) for i in self.smiles]
        fp = [AllChem.GetMorganFingerprintAsBitVect(x,3) for x in ms]
        return fp

    def topological_fp(self):
        ms =[Chem.MolFromSmiles(i) for i in self.smiles]
        fp = [FingerprintMols.FingerprintMol(x) for x in ms]
        return fp

    def atom_pair_fp(self):
        ms = [Chem.MolFromSmiles(i) for i in self.smiles]
        fp = [Pairs.GetAtomPairFingerprintAsIntVect(x) for x in ms]
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
