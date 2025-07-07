<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

// Form state
const title = ref('');
const content = ref('');
const errorMessage = ref('');

const router = useRouter();

async function createNote() {
  // Reset error message
  errorMessage.value = '';

  // Basic validation
  if (!title.value.trim() && !content.value.trim()) {
    errorMessage.value = 'You must provide a title and content.';
    return;
  }

  if (!title.value.trim()) {
    errorMessage.value = 'You must provide a title.';
    return;
  }

  if (!content.value.trim()) {
    errorMessage.value = 'The content cannot be empty.';
    return;
  }

  // useFetch for POST request
  const { error } = await useFetch('http://127.0.0.1:8000/api/notes/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: {
      title: title.value,
      content: content.value,
    },
  });

  if (error.value) {
    // If the API returns an error, display it
    errorMessage.value = `Failed to create note: ${error.value.data || error.value.message}`;
  } else {
    // On success, navigate back to the home page
    router.push('/');
  }
}
</script>

<template>
  <div class="max-w-2xl mx-auto">
    <h2 class="text-2xl font-semibold mb-4">Create a New Note</h2>
    <form class="space-y-6" @submit.prevent="createNote">
      <div>
        <Label for="title" class="text-lg">Title</Label>
        <Input
          id="title"
          v-model="title"
          type="text"
          placeholder="Enter the title"
          class="mt-2 text-base"
        />
      </div>
      <div>
        <Label for="content" class="text-lg">Content</Label>
        <Textarea
          id="content"
          v-model="content"
          placeholder="What's on your mind?"
          class="mt-2 text-base"
          rows="10"
        />
      </div>

      <!-- Error Message Display -->
      <div v-if="errorMessage" class="text-red-500">
        {{ errorMessage }}
      </div>

      <div class="flex justify-end gap-4">
        <NuxtLink to="/">
          <Button type="button" variant="outline">Cancel</Button>
        </NuxtLink>
        <Button type="submit">
          Save Note
        </Button>
      </div>
    </form>
  </div>
</template>