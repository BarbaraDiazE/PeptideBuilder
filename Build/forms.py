from django import forms
from multiselectfield import MultiSelectField

from Build.models import First,Linear, Methylated, Topology

class InputForm(forms.ModelForm):
    class Meta:
        model = First      
        fields = ("first",)
        
class InputForm1(forms.ModelForm):
    class Meta:
        model = Linear      
        fields = ("linear",)  

class InputForm2(forms.ModelForm):
    class Meta:
        model = Methylated      
        fields = ("methylated",)  

class TopologyForm(forms.ModelForm):
    class Meta:
        model = Topology
        fields = ("topology", "length")