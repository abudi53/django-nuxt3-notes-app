<script setup lang="ts">
import type { Note } from '@/types';

// useFetch is Nuxt's primary way to fetch data.
// It's SSR-friendly and has great features for handling loading, errors, etc.
const { data: notes, pending, error } = await useFetch<Note[]>('http://127.0.0.1:8000/api/notes/');

// A simple function to format the date string
function formatDate(dateString: string) {
  const options: Intl.DateTimeFormatOptions = {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  };
  return new Date(dateString).toLocaleDateString(undefined, options);
}
</script>

<template>
  <div>
    <!-- 1. Loading State -->
    <div v-if="pending">
      <p>Loading notes...</p>
    </div>

    <!-- 2. Error State -->
    <div v-else-if="error">
      <p class="text-red-500">Error fetching notes: {{ error.message }}</p>
    </div>

    <!-- 3. Success State (with notes) -->
    <div v-else-if="notes && notes.length" class="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
      <NuxtLink v-for="note in notes" :key="note.id" :to="`/notes/${note.id}`">
      <Card>
        <CardHeader>
          <CardTitle>{{ note.title }}</CardTitle>
        </CardHeader>
        <CardContent>
          <p class="line-clamp-3">
            {{ note.content }}
          </p>
        </CardContent>
        <CardFooter class="text-sm text-muted-foreground">
          <p>Last updated: {{ formatDate(note.updated_at) }}</p>
        </CardFooter>
      </Card>
      </NuxtLink>
    </div>

    <!-- 4. Success State (no notes) -->
    <div v-else>
      <p>No notes found. Create one to get started!</p>
    </div>
  </div>
</template>