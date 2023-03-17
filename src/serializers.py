from rest_framework import serializers
from src.models import *


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = team_member
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    members = TeamMemberSerializer(many=True)

    class Meta:
        model = projects
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    projects_part = ProjectSerializer(many=True)

    class Meta:
        model = member
        fields = '__all__'
