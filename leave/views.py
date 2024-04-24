from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import LeaveRequestForm,LeaveApprovalForm
from .models import LeaveRequest
from django.contrib import messages
from employee.models import Employee



# Create your views here.
def leaverequest(request):
    form=LeaveRequestForm()
    if request.method== "POST":
        print(request.POST) 
        form=LeaveRequestForm(request.POST)
        if form.is_valid():
             form.instance.employee=request.user
             form.save()
             return redirect('table')
        else:
            form=LeaveRequestForm()
            return render(request, 'leaverequest.html',{'form':form})
    return render(request, 'leaverequest.html',{'form':form})



def request_table(request):
    requests=LeaveRequest.objects.all()
    items_per_page=10
    paginator=Paginator(requests, items_per_page)
    page_number=request.GET.get('page')
    try:
        requests=paginator.page(page_number)
    except PageNotAnInteger:
        requests=paginator.page(1)
    except EmptyPage:
        requests=paginator.page(paginator.num_pages)
    return render (request, 'request-table.html',{'requests':requests})

def leave_approved(self):
		return self.is_approved == True

def approve_leave(request, pk):
    request=get_object_or_404(LeaveRequest, id=pk)
    if not request.is_approved:  # Check if leave request is not already approved
        request.status = 'approved'
        request.is_approved = True
        request.save()
        return redirect('table')
   
    return redirect('table') 

    



