from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Issue,Comment
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

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
    

    return render(request,'issues/dashboard.html')


def onebug(request, issue_id):
    issue= get_object_or_404(Issue, pk=issue_id)
    comments = Comment.objects.filter(issue=issue).order_by('-id')
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        context = {
        'issue':issue,
        'comments' : comments,
        'comment_form' : comment_form,


    }
        if comment_form.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(issue=issue,user=request.user, content=content )
            comment.save()
            return render(request, 'issues/onebug.html',context)

           

    else:
        comment_form=CommentForm()

    
    
    
    context = {
        'issue':issue,
        'comments' : comments,
        'comment_form' : comment_form,


    }
    return render(request, 'issues/onebug.html',context)

def issued_by_me(request):
    issues = Issue.objects.filter(issuer_username = request.user.username ).order_by('deadline')
    
    paginator = Paginator(issues, 4)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)
    
    context = {
        'issues': paged_listing
    }

    return render(request,'issues/issued_by_me.html', context)


def assigned_to_me(request):
    issues = Issue.objects.filter(assigned_to_username= request.user.id ).order_by('deadline')
    
    paginator = Paginator(issues, 4)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)
    
    context = {
        'issues': paged_listing
    }


    return render(request,'issues/assigned_to_me.html', context)










        

    
       



       
    




