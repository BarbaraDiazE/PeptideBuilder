from django import forms
from multiselectfield import MultiSelectField

from Build.models import First,Linear, Methylated, Topology, Keys

    
class InputForm(forms.Form):
    first = forms.ChoiceField(
        choices=Keys,
    )
        
#class InputForm1(forms.ModelForm):
#    class Meta:
#        model = Linear      
#        fields = ("linear",)  
class InputForm1(forms.Form):
    linear = forms.MultipleChoiceField(
        choices= Keys,
        #widget = forms.SelectMultiple
    )

class InputForm2(forms.ModelForm):
    class Meta:
        model = Methylated      
        fields = ("methylated",)  

class TopologyForm(forms.ModelForm):
    class Meta:
        model = Topology
        fields = ("topology", "length")