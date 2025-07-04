from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing notes.
    """

    queryset = Note.objects.all().order_by("-updated_at")
    serializer_class = NoteSerializer
