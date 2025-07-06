<script setup lang="ts">
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import type { Note } from '@/types';

const route = useRoute();
const router = useRouter();
const noteId = route.params.id;

// Refs for note data and form state
const note = ref<Note | null>(null);
const editTitle = ref('');
const editContent = ref('');
const isEditing = ref(false);
const errorMessage = ref('');

// Fetch the single note's data when the component mounts
const { data, error: fetchError } = await useFetch<Note>(`http://127.0.0.1:8000/api/notes/${noteId}/`);

if (fetchError.value) {
  errorMessage.value = "Failed to load note. It may have been deleted.";
} else {
  note.value = data.value;
  // Pre-fill edit fields
  editTitle.value = note.value?.title || '';
  editContent.value = note.value?.content || '';
}

// Function to switch to edit mode
function startEditing() {
  isEditing.value = true;
}

// Function to cancel editing
function cancelEditing() {
  isEditing.value = false;
  // Reset form fields to original values
  if (note.value) {
    editTitle.value = note.value.title;
    editContent.value = note.value.content;
  }
}

// Function to update the note
async function updateNote() {
  if (!note.value) return;

  const { data: updatedNote, error } = await useFetch<Note>(`http://127.0.0.1:8000/api/notes/${noteId}/`, {
    method: 'PUT',
    body: {
      title: editTitle.value,
      content: editContent.value,
    },
  });

  if (error.value) {
    errorMessage.value = 'Failed to update note.';
  } else {
    note.value = updatedNote.value;
    isEditing.value = false; // Exit edit mode on success
  }
}

// Function to delete the note
async function deleteNote() {
  const { error } = await useFetch(`http://127.0.0.1:8000/api/notes/${noteId}/`, {
    method: 'DELETE',
  });

  if (error.value) {
    errorMessage.value = 'Failed to delete note.';
  } else {
    // On successful deletion, navigate back to the home page
    router.push('/');
  }
}
</script>

<template>
  <div class="max-w-3xl mx-auto">
    <NuxtLink to="/" class="text-primary hover:underline mb-4 inline-block">
      ← Back to all notes
    </NuxtLink>
    <!-- Error Display -->
    <div v-if="errorMessage && !note" class="text-red-500 p-4 border border-red-500 rounded-md">
      {{ errorMessage }}
      <NuxtLink to="/" class="text-blue-500 underline ml-2">Go Home</NuxtLink>
    </div>

    <!-- Main Content -->
    <div v-else-if="note">
      <!-- View Mode -->
      <div v-if="!isEditing" class="space-y-6">
        <div class="flex justify-between items-start">
          <h1 class="text-4xl font-bold">{{ note.title }}</h1>
          <div class="flex gap-2">
            <Button @click="startEditing">Edit</Button>
            <AlertDialog>
              <AlertDialogTrigger as-child>
                <Button variant="destructive">Delete</Button>
              </AlertDialogTrigger>
              <AlertDialogContent>
                <AlertDialogHeader>
                  <AlertDialogTitle>Are you absolutely sure?</AlertDialogTitle>
                  <AlertDialogDescription>
                    This action cannot be undone. This will permanently delete the note.
                  </AlertDialogDescription>
                </AlertDialogHeader>
                <AlertDialogFooter>
                  <AlertDialogCancel>Cancel</AlertDialogCancel>
                  <AlertDialogAction @click="deleteNote">Continue</AlertDialogAction>
                </AlertDialogFooter>
              </AlertDialogContent>
            </AlertDialog>
          </div>
        </div>
        <p class="text-lg whitespace-pre-wrap">{{ note.content }}</p>
        <p class="text-sm text-muted-foreground">Last updated: {{ new Date(note.updated_at).toLocaleString() }}</p>
      </div>

      <!-- Edit Mode (Form) -->
      <form v-else class="space-y-6" @submit.prevent="updateNote">
        <div>
          <Label for="title" class="text-lg">Title</Label>
          <Input id="title" v-model="editTitle" type="text" class="mt-2 text-base" />
        </div>
        <div>
          <Label for="content" class="text-lg">Content</Label>
          <Textarea id="content" v-model="editContent" class="mt-2 text-base" rows="10" />
        </div>
        <div class="flex justify-end gap-4">
          <Button type="button" variant="outline" @click="cancelEditing">Cancel</Button>
          <Button type="submit">Save Changes</Button>
        </div>
      </form>
    </div>

    <!-- Loading State -->
    <div v-else>
      <p>Loading note...</p>
    </div>
  </div>
</template>