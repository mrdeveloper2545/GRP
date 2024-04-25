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
    requests=LeaveRequest.objects.filter(status='pending')
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



def approve_leave(request, pk):
    request=get_object_or_404(LeaveRequest, id=pk)
    if  request.status != 'approved': 
        request.status = 'approved'
        request.save()
        return redirect('table')
    return redirect('table') 

def reject_leave(request, pk):
    request=get_object_or_404(LeaveRequest, id=pk)
    if request.status != 'rejected':
          request.status = 'rejected'
          request.save()
          return redirect ('table')
    return redirect ('table')

def approved_list(request):
     approve_requests=LeaveRequest.objects.filter(status='approved')
     items_per_page = 5
     paginator=Paginator(approve_requests, items_per_page)
     page_number=request.GET.get('page')
     try:
          approve_requests=paginator.page(page_number)
     except PageNotAnInteger:
          approve_requests=paginator.page(1)
     except EmptyPage:
          approve_requests=paginator.page(paginator.num_pages)
     return render(request, 'approve.html', {'approve_requests':approve_requests})

def rejected_list(request):
    rejected_requests=LeaveRequest.objects.filter(status='rejected')
    items_per_page=10
    paginator=Paginator(rejected_requests, items_per_page)
    page_number=request.GET.get('page')
    try:
        rejected_requests=paginator.page(page_number)
    except PageNotAnInteger:
        rejected_requests=paginator.page(1)
    except EmptyPage:
        rejected_requests=paginator.page(paginator.num_pages)
    return render(request, 'reject.html', {'rejected_requests':rejected_requests})    
     

    



