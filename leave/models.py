from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime



# Create your models here.
SICK='sick'
EMERGANCY='emargancy'
MARTENITY='martenity'
STUDY='study'

LEAVE_TYPE=(
    (SICK, 'Sick leave'),
    (EMERGANCY, 'Emergancy leave'),
    (MARTENITY, 'Martenity leave'),
    (STUDY, 'Study leave'),
)

DAYS=30
    
class Leave(models.Model):
	employee=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
	startdate = models.DateField(verbose_name=_('start Date'),help_text='leave start date is on...',null=True,blank=False)
	enddate = models.DateField(verbose_name=_('End Date'),help_text='coming back on ...',null=True,blank=False)
	leavetype = models.CharField(choices=LEAVE_TYPE,max_length=25,default=SICK,null=True,blank=False)
	reason = models.CharField(verbose_name=_('Reason for Leave'),max_length=255,help_text='add additional information for leave',null=True,blank=True)
	defaultdays = models.PositiveIntegerField(verbose_name=_('Leave days per year counter'),default=DAYS,null=True,blank=True)
	status=models.CharField(max_length=12,default='pending')
	is_approved=models.BooleanField(default=False)
	updated=models.DateTimeField(auto_now=True,auto_now_add=False)
	created=models.DateTimeField(auto_now=False,auto_now_add=True)


	def save(self, *args, **kwargs):
		if self.startdate and self.enddate:
			self.defaultdays -= (self.enddate-self.startdate).days
			super(Leave, self).save(*args, **kwargs)






	
	class Meta:
		verbose_name = _('Leave')
		verbose_name_plural = _('Leaves')
		ordering = ['-created'] #recent objects



	def __str__(self):
		return ('{0} - {1}'.format(self.leavetype,self.employee))	




   


	



  

