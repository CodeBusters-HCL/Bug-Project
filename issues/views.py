from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Issue

# Create your views here.

def report_issue(request):

    

    if request.method =='POST':

        
        if request.user.is_authenticated:
            issuer_username = request.user.username
            issuer_email = request.user.email
        
            issue_title = request.POST['issue_title']
            project_type = request.POST['project_type']
            priority = request.POST['priority']
            deadline = request.POST['deadline']
            severity = request.POST['severity']
            issue_file = request.POST['issue_file']
            description = request.POST['description']

            issue= Issue.objects.create(issuer_username=issuer_username,issuer_email=issuer_email,issue_title=issue_title,project_type=project_type,priority=priority,deadline=deadline,severity=severity,issue_file=issue_file,description=description)
            issue.save()
            messages.success(request, 'Bug Issue Submitted sucsessfully.')
            return redirect('dashboard')

        else:
            messages.error(request,'Invalid Bug')
            return render(request,'issues/report_issue.html')

    else:
        return render(request,'issues/report_issue.html')



def dashboard(request):
    issues = Issue.objects.filter(issuer_username = request.user.username )
    context = {
        'issues': issues
    }
    return render(request,'issues/dashboard.html', context)







        

    
       



       
    




