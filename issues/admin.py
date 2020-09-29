from django.contrib import admin

# Register your models here.

from .models import Issue

class IssueAdmin(admin.ModelAdmin):
    list_display = ('issue_title','issued_on' ,'issuer_username','issuer_email','project_type','priority', 'deadline', 'severity', 'description','issue_status', 'assigned_to_email', 'assigned_to_username' )
    list_display_links = ('issue_title','issued_on' ,'issuer_username')
    list_editable = ( 'assigned_to_email', 'assigned_to_username','issue_status','priority',)
    list_filter = ('severity','issue_status','priority',)
    search_fields=('issue_title','issued_on' ,'issuer_username','issuer_email','project_type','priority', 'deadline', 'severity', 'description','issue_status', 'assigned_to_email', 'assigned_to_username')
    list_per_page=25

admin.site.register(Issue, IssueAdmin)


    
   
    
    