import rdkit
from rdkit import Chem
from rdkit.Chem import Descriptors

import numpy as np 
import pandas as pd 

def compute_descriptors(smiles):
    smiles = list(map(lambda x: Chem.MolFromSmiles(x), smiles))
    HBA = list(map(lambda x: Descriptors.NumHAcceptors(x), smiles))
    HBD = list(map(lambda x:Descriptors.NumHDonors(x), smiles))
    RB = list(map(lambda x: Descriptors.NumRotatableBonds(x), smiles)) 
    LOGP =  list(map(lambda x: Descriptors.MolLogP(x), smiles))
    TPSA =  list(map(lambda x: Descriptors.TPSA(x), smiles))
    MW = list(map(lambda x: Descriptors.MolWt(x), smiles))
    
    return HBA, HBD, RB, LOGP, TPSA, MW