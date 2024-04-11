from typing import Any
from django import forms
from .models import Leave
import datetime
import pytz


class LeaveCreationForm(forms.ModelForm):
    startdate=forms.DateTimeField(widget=forms.DateInput(attrs={"type": "date",'class':'form-control'}))
    enddate=forms.DateTimeField(widget=forms.DateInput(attrs={"type": "date",'class':'form-control'}))
    reason=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    


    class Meta:
        model = Leave
        exclude = ['employee','defaultdays','hrcomments','status','is_approved','updated','created']


    def clean(self):
        cleaned_data = super().clean()
        enddate = cleaned_data.get('enddate')
        startdate = cleaned_data.get('startdate')

        if startdate and enddate:
            if startdate > enddate:
                raise forms.ValidationError("check the datefield correct")
            
    def save(self, commit=True):
            leave_request=super().save(False)
            startdate=self.cleaned_data.get('startdate')
            enddate=self.cleaned_data.get('enddate')

            if startdate and enddate:
              leave_request.days.used=(enddate - startdate).days +1 
   
              if commit:
                leave_request.save()

            return leave_request
        

   