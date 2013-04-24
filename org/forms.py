'''
Created on 2013-4-24

@author: wwjiang
'''

from django import forms

class MessageForm(forms.Form):
    content = forms.CharField(
            widget=forms.Textarea(attrs={
                'id':'comment-area',
                'cols':'100',
                'rows':'14',
                }),
            label="ÄÚÈÝ")
