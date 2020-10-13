from .models import Issue,Comment
from django.contrib.auth.models import User
from django import forms
# from .models import Issue


class CommentForm(forms.ModelForm):
    class Meta:
        model =Comment
        fields = ('content',)


# class BugForm(forms.ModelForm):

#     class Meta:
#         model = Issue
#         fields = ('issue_title', 'project_type', 'priority', 'severity', 'deadline', 'description', 'issue_file', )








