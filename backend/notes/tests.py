import pytest
from django.urls import reverse
from rest_framework import status
from .models import Note

# The @pytest.mark.django_db marker is essential to allow database access for the test.
# The `client` fixture is provided by pytest-django to make API requests.


@pytest.mark.django_db
def test_get_all_notes(client):
    """
    Ensure we can retrieve a list of notes.
    """
    # Create some data for this specific test
    Note.objects.create(title="First Note", content="Content 1")
    Note.objects.create(title="Second Note", content="Content 2")

    url = reverse("note-list")
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2


@pytest.mark.django_db
def test_get_single_note(client):
    """
    Ensure we can retrieve a single note by its ID.
    """
    note = Note.objects.create(title="A Single Note", content="Some content")
    url = reverse("note-detail", kwargs={"pk": note.pk})
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == note.title


@pytest.mark.django_db
def test_create_note(client):
    """
    Ensure we can create a new note object.
    """
    url = reverse("note-list")
    data = {"title": "New Test Note", "content": "Some new content."}
    response = client.post(url, data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert Note.objects.count() == 1
    assert Note.objects.get().title == "New Test Note"


@pytest.mark.django_db
def test_update_note(client):
    """
    Ensure we can update an existing note object.
    """
    note = Note.objects.create(title="Original Title", content="Original content")
    url = reverse("note-detail", kwargs={"pk": note.pk})
    updated_data = {"title": "Updated Title", "content": "Updated content."}
    response = client.put(url, updated_data, content_type="application/json")

    # Refresh the object from the database to check the update
    note.refresh_from_db()

    assert response.status_code == status.HTTP_200_OK
    assert note.title == "Updated Title"


@pytest.mark.django_db
def test_delete_note(client):
    """
    Ensure we can delete a note object.
    """
    note = Note.objects.create(title="To Be Deleted", content="Delete me")
    url = reverse("note-detail", kwargs={"pk": note.pk})
    response = client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Note.objects.count() == 0


@pytest.mark.django_db
def test_create_note_with_missing_title(client):
    """
    Ensure creating a note with no title fails with a 400 Bad Request.
    """
    url = reverse("note-list")
    data = {"content": "This note has no title."}
    response = client.post(url, data, format="json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
