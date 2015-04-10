# In forms.py...
#REF: https://docs.djangoproject.com/en/1.7/topics/http/file-uploads/
from django import forms

class UploadFileForm(forms.Form):

	docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
    #title = forms.CharField(max_length=50)
    #file = forms.FileField()