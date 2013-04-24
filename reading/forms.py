'''
Created on 2013-4-24

@author: wwjiang
'''
from django import forms

class ReadingNoteForm(forms.Form):
    title = forms.CharField(max_length=30,
            widget=forms.TextInput(attrs={'tabindex':'2'}),
            label="±êÌâ")
    content = forms.CharField(
            widget=forms.Textarea(attrs={
                'id':'comment-area',
                'cols':'100',
                'rows':'14',
                }),
            label="ÄÚÈÝ")
