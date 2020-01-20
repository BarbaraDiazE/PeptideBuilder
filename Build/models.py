from django.db import models
from django import forms
from multiselectfield import MultiSelectField

class AminoAcid(models.Model):
    amino_acid = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.amino_acid
    
class DataAminoAcids(models.Model):
    name = models.ForeignKey(AminoAcid, on_delete=models.PROTECT, related_name='data')
    first_smile = models.CharField(max_length=264)
    first_abbreviation = models.CharField(max_length=5)
    linear_smile = models.CharField(max_length=264)
    linear_abbreviation = models.CharField(max_length=5)
    methylated_smile = models.CharField(max_length=264)
    methylated_abbreviation = models.CharField(max_length=5)
    
    def __str__(self):
        return self.name.amino_acid

class Oxygen(models.Model):
    oxygen_id = models.IntegerField(primary_key=True)
    linear = models.CharField(max_length=264)
    cyclic = models.CharField(max_length=264)
    
Keys = (
            ("ALA", 'ALA'),
            ("CYS", "CYS"),
            ("ASP", "ASP"),
            ("GLU", "GLU"), 
            ("PHE", "PHE"),
            ("HIS", "HIS"),
            ("ILE", "ILE"),
            ("LYS", "LYS"),
            ("LEU", "LEU"),
            ("MET", "MET"),
            ("ASN", "ASN"),
            ("PRO", "PRO"), 
            ("GLN", "GLN"),
            ("ARG", "ARG"),
            ("SER", "SER"),
            ("THR", "THR"),
            ("VAL", "VAL"),
            ("TRP", "TRP"),
            ("TYR", "TYR"),
             ("GLY", "GLY")
                )
topology = (("linear", "linear"),
            ("cyclic", "cyclic"))

class First(models.Model):
    first = MultiSelectField(verbose_name="First position", choices=Keys, max_choices=1)
    
class Linear(models.Model):
    linear = MultiSelectField(verbose_name="Linear structure", choices=Keys, max_choices=20)

class Methylated(models.Model):
    methylated = MultiSelectField(verbose_name="Methylated structure", choices=Keys, max_choices=20)
   
class Topology(models.Model):
    topology = MultiSelectField(verbose_name= "Topology", choices=topology, max_choices=2)
    length = models.IntegerField(verbose_name="length", name= "length", max_length= 6)