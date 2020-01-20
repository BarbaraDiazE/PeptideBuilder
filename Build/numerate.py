"""Numerate peptides from amino acids"""
from .amino_acid import dict_amino_acid
from .models import AminoAcid, DataAminoAcids, Oxygen
from Build.combinations import combine_linear_smiles, combine_cyclic_smiles, combine_abbreviations

class Numerate:

    def __init__(self, first , linear, methylated, topology, length):
        self.first = first
        self.linear = linear
        self.methylated = methylated
        self.topology = topology
        self.length = length
        print("soy clase numerate")
    
    def get_first(self):
        _ = AminoAcid.objects.filter(amino_acid = self.first)[0]
        first = DataAminoAcids.objects.filter(name = _).all()[0].first_smile
        return first

    def get_dataset(self):
        linear_qs = AminoAcid.objects.filter(amino_acid__in=self.linear)\
            .values_list('data__linear_smile')
        methylated_qs = AminoAcid.objects.filter(amino_acid__in=self.methylated)\
            .values_list('data__methylated_smile')
        linear_dataset = list(map(lambda x: x[0], linear_qs))
        methylated_dataset = list(map(lambda x: x[0], methylated_qs))
        dataset = linear_dataset + methylated_dataset
        return dataset
    
    def get_abreviations(self):
        _ = AminoAcid.objects.filter(amino_acid = self.first)[0]
        first_abbreviation = DataAminoAcids.objects.filter(name = _).all()[0].first_abbreviation
        linear_abbreviations_qs = AminoAcid.objects.filter(amino_acid__in=self.linear)\
            .values_list('data__linear_abbreviation')
        methylated_abbreviations_qs = AminoAcid.objects.filter(amino_acid__in=self.methylated)\
            .values_list('data__methylated_abbreviation')
        linear_abbreviations = list(map(lambda x: x[0], linear_abbreviations_qs))
        methylated_abbreviations = list(map(lambda x: x[0], methylated_abbreviations_qs))
        abbreviations = linear_abbreviations + methylated_abbreviations
        return first_abbreviation, abbreviations
        
        
    def get_oxygen(self):
        linear = str()
        linear = Oxygen.objects.filter(oxygen_id = self.length)[0].linear
        cyclic = str()
        cyclic = Oxygen.objects.filter(oxygen_id = self.length)[0].cyclic
        return linear, cyclic
        

    def numerate(self):
        first = self.get_first()
        dataset = self.get_dataset()
        first_abbreviation, abbreviations = self.get_abreviations()
        linear, cyclic = self.get_oxygen()
        linear_peptides = list()
        cyclic_peptides = list()
        for i in range(len(self.topology)):
            if (self.topology[i]) == "linear":
                linear_peptides = combine_linear_smiles(first, dataset, self.length, linear)
                linear_abbreviations = combine_abbreviations(first_abbreviation, abbreviations, self.length)
            elif (self.topology[i]) == "cyclic":
                cyclic_peptides = combine_cyclic_smiles(first, dataset, self.length, cyclic)
                cyclic_abbreviations = combine_abbreviations(first_abbreviation, abbreviations, self.length)
            
        return linear_peptides, cyclic_peptides, linear_abbreviations, cyclic_abbreviations  

    def write_databases(self):
        linear_peptides, cyclic_peptides, linear_abbreviations, cyclic_abbreviations   = self.numerate()
        print("linear_peptides", linear_peptides[10])
        print("linear_abbreviations", linear_abbreviations[10])
        print("cyclic_peptides", cyclic_peptides[10])