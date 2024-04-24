from django.db import models
from django.contrib.auth.models import User
from dateutil.parser import parse

# Create your models here.

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

DAYS = 30

class LeaveRequest(models.Model):
    employee=models.ForeignKey(User, on_delete=models.CASCADE)
    startdate = models.DateField(verbose_name=('Start Date'),help_text='leave start date is on ..',null=True,blank=False)
    enddate = models.DateField(verbose_name=('End Date'),help_text='coming back on ...',null=True,blank=False)
    leavetype = models.CharField(choices=LEAVE_TYPE,max_length=25,default=SICK,null=True,blank=False)
    reason = models.CharField(verbose_name=('Reason for Leave'),max_length=255,help_text='add additional information for leave',null=True,blank=True)
    defaultdays = models.PositiveIntegerField(verbose_name=('Leave days per year counter'),default=DAYS,null=True,blank=True)



    status = models.CharField(max_length=12,default='pending') #pending,approved,rejected,cancelled
    is_approved = models.BooleanField(default=False) #hide

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)


    def save(self):
        if self.startdate and self.enddate:
           self.defaultdays = (self.enddate - self.startdate).days + 1
        super(LeaveRequest, self).save()

       

    def __str__(self):
        return self.employee.username
    


    def approve(self):
       if not self.is_approved:
           self.is_approved == True
           self.status ='approved'
           self.save()
        

   




    










