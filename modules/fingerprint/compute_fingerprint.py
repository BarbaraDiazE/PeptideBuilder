"""Compute Fingerprint"""
import numpy as np
import itertools as it
import random

import rdkit    
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem, MACCSkeys
from rdkit.Chem.Fingerprints import FingerprintMols

class FP:
    
    def__init__(self, csv, parameter):
        self.csv = csv
        self.parameter = parameter

    def maccskeys_fp(Library):
        ms=[Chem.MolFromSmiles(i) for i in SMILES]
        matrix_fp = [MACCSkeys.GenMACCSKeys(x) for x in ms]
        return matrix_fp


    def compute(self):
        if parameter == "MACCS Keys":
            matrix_fp = self.maccskeys_fp()
        return matrix_fp
