<template>
  <div>
    <Body class="bg-background text-foreground" />
    <div class="container mx-auto p-4">
      <div class="flex justify-between items-center mb-6">
        <h1 class="text-3xl font-bold mb-6">My Notes App</h1>
        <NuxtLink to="/notes/new">
          <Button>New Note</Button>
        </NuxtLink>
      </div>
      <NuxtPage />
    </div>
  </div>
</template>