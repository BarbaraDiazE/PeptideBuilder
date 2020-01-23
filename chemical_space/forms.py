from django import forms
from chemical_space.models import FP, PP, Descriptors, FP_Keys, PP_Keys
from multiselectfield import MultiSelectField

class PCA_FP_Form(forms.ModelForm):
    class Meta:
        model = FP
        fields = ( "pca_fp",)


class TSNE_FP_Form(forms.ModelForm):
    class Meta:
        model = FP
        fields = ( "tsne_fp",)

class PCA_PP_Form(forms.ModelForm):
    class Meta:
        model = PP
        fields = ( "pca_pp",)


class TSNE_PP_Form(forms.ModelForm):
    class Meta:
        model = PP
        fields = ( "tsne_pp",)

class Chem_space_form(forms.ModelForm):
    class Meta:
        model = Descriptors
        fields = ( "pca_fp", "tsne_fp", "pca_pp", "tsne_pp",)

#class Chem_space_form(forms.Form):
#    pca_fp = forms.MultipleChoiceField(choices=FP_Keys, required= False)
#    tsne_fp = forms.MultipleChoiceField( choices=FP_Keys,  required= False)
#    pca_pp = forms.MultipleChoiceField( choices=PP_Keys,  required= False)
#    tsne_pp = forms.MultipleChoiceField(choices=PP_Keys,  required= False)    
