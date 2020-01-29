import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PeptideBuilder.settings')

import django
django.setup()

from Build.models import AminoAcid, DataAminoAcids
from modules.build.amino_acid import dict_amino_acid

data = dict_amino_acid
list_aminoacids = ["ALA", "CYS", "ASP", "GLU", "PHE", "HIS",  "ILE", "LYS", "LEU", "MET", "ASN", "PRO", "GLN", "ARG", "SER", "THR", "VAL", "TRP", "TYR", "GLY"]
def add_aminoacid(amino):
    A = AminoAcid.objects.get_or_create(amino_acid = amino)[0]
    A.save()
    return A

def populate(amino):
    a = DataAminoAcids(
                name = add_aminoacid(amino),
                first_smile = data[amino]["first_smile"],
                first_abbreviation = data[amino]["first_abbreviation"],
                linear_smile = data[amino]["linear_smile"],
                linear_abbreviation = data[amino]["linear_abbreviation"],
                methylated_smile = data[amino]["methylated_smile"],
                methylated_abbreviation = data[amino]["methylated_abbreviation"]
    )
    a.save()
    return a 
if __name__ == "__main__":
    for i in range(len(list_aminoacids)):
        populate(list_aminoacids[i])
print("population is done")