from time import sleep
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from tasks import sync_function, add_numbers
from .serializers import UserSerializer, GroupSerializer
from asgiref.sync import sync_to_async
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    @sync_to_async
    def get(self, request, format=None):
        # sync_to_async(sync_function)()
        # async_function = sync_to_async(sync_function, thread_sensitive=True)
        # async_function()
        return Response("data served")


@api_view(["GET"])
def sample_view(request):
    # sync_function()
    sync_function.schedule(delay=1)
    return Response("data served")
