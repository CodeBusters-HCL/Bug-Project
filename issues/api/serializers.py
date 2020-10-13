from rest_framework import serializers
from issues.models import Issue

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'

class IssueCreateSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Issue
        fields = ['issue_title', 'project_type', 'priority', 'severity', 'deadline', 'description', 'issue_file']

        issuer_username = serializers.ReadOnlyField(source='issuer.username')
        issuer_email = serializers.ReadOnlyField(source='issuer.email')



    def create(self,validated_data):
        issuer_username=issuer_username
        issuer_email=issuer_email
        user = Issue.objects.create(
                    issuer_username=issuer_username,
                    issuer_email=issuer_email,
                    issue_title=self.validated_data['issue_title'],
                    project_type=self.validated_data['project_type'],
                    priority=self.validated_data['priority'],
                    severity=self.validated_data['severity'],
                    deadline=self.validated_data['deadline'],
                    description=self.validated_data['description'],
                    issue_file=self.validated_data['issue_file'],
                )
        user.set_password(password)
        user.save()
        return user
