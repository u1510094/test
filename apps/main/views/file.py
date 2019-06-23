from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from main.models import File
from main.serializers.file import FileModelSerializer


class FileViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    """
        retrieve:
        Return object of File

        list:
        Return a list of File objects

        create:
        Create a new  instance of File
    """
    model = File
    queryset = File.objects.all()
    serializer_class = FileModelSerializer
