from django import forms
from leave.models import LeaveRequest
import datetime



SICK = 'sick'
CASUAL = 'casual'
EMERGENCY = 'emergency'
STUDY = 'study'
MATERNITY = 'maternity'
BEREAVEMENT = 'bereavement'
QUARANTINE = 'quarantine'
COMPENSATORY = 'compensatory'
SABBATICAL = 'sabbatical'

LEAVE_TYPE = (
(SICK,'Sick Leave'),
(CASUAL,'Casual Leave'),
(EMERGENCY,'Emergency Leave'),
(STUDY,'Study Leave'),
(MATERNITY, 'Maternity Leave'),
(BEREAVEMENT, 'Bereavement Leave'),
(QUARANTINE, 'Self Quarantine'),
(COMPENSATORY, 'Compensatory Leave'),
(SABBATICAL, 'Sabbatical Leave')
)
class LeaveRequestForm(forms.ModelForm):
   reason = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','rows': 2, 'cols': 40}))
   startdate=forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))
   enddate=forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))
   leavetype=forms.ChoiceField(choices=LEAVE_TYPE,widget=forms.Select(attrs={'class':'form-control'}))
   class Meta:
    model = LeaveRequest
    exclude = ['employee','defaultdays','hrcomments','status','is_approved','updated','created']


    def save(self, commit=True):
       leave_request=super().save(commit=False)
       leave_request.user=self.cleaned_data['user']
       if commit:
          leave_request.save()
       return leave_request
    
  
   
     

   # def clean_enddate(self):
   #     startdate=self.cleaned_data['startdate']
   #     enddate=self.cleaned_data['enddate']
   #     today_date=datetime.date.today()

   #     if startdate < today_date or enddate < today_date :
   #        raise forms.ValidationError("Selected dates are incorrect, please select again")
       
   #     if startdate >= enddate or startdate >= today_date and enddate >= today_date:
   #        raise forms.ValidationError("Selected dates are wrong")
       
   #     return enddate




class LeaveApprovalForm(forms.ModelForm):
    status=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = LeaveRequest
        fields = ['status', 'is_approved']
        

       
           
        
