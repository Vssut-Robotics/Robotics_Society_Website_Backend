from src.serializers import MemberSerializer
from src.models import member
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


@api_view(["GET"])
def getMembers(request):
    query = request.query_params.get('year')
    if (query == None):
        query = ''
    print(query)
    members = member.objects.filter(year__icontains=query)
    serializer = MemberSerializer(members, many=True)
    return Response(serializer.data)


def getMember(request, pk):
    query = member.objects.get(_id=pk)
    serializer = MemberSerializer(query, many=False)
    return Response(serializer.data)
