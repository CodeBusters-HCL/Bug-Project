from django.contrib import admin

# Register your models here.

from .models import Issue,Comment

class IssueAdmin(admin.ModelAdmin):
    list_display = ('issue_title','issued_on' ,'issuer_username','issuer_email','project_type','priority', 'deadline', 'severity', 'issue_status', )
    list_display_links = ('issue_title','issued_on' ,'issuer_username','issuer_email')
    list_editable = ('issue_status','priority',)
    list_filter = ('severity','issue_status','priority',)
    search_fields=('issue_title','issued_on' ,'issuer_username','issuer_email','project_type','priority', 'deadline', 'severity', 'description','issue_status', 'assigned_to_email', 'assigned_to_username')
    
admin.site.register(Comment)
admin.site.register(Issue, IssueAdmin)




    
   
    
    