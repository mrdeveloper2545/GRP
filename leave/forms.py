from django import forms
from leave.models import LeaveRequest


class LeaveRequestForm(forms.ModelForm):
   reason = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','rows': 2, 'cols': 40}))
   class Meta:
    model = LeaveRequest
    exclude = ['employee','defaultdays','hrcomments','status','is_approved','updated','created']
   
   def save(self, commit=True):
     defaultdays=super().save(commit=False)
     startdate=self.cleaned_data['startdate']
     enddate=self.cleaned_data['enddate']
     if enddate > startdate:
       return defaultdays==enddate-startdate
     else:
       return None
       
           
        
