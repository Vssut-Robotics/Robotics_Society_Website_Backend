from src.serializers import MemberSerializer, ProjectSerializer
from src.models import projects
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


@api_view(["GET"])
def getProjects(request):
    query = projects.objects.all()
    serializer = ProjectSerializer(query, many=True)
    return Response(serializer.data)


def getProject(request, pk):
    query = projects.objects.get(_id=pk)
    serializer = ProjectSerializer(query, many=False)
    return Response(serializer.data)
