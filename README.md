# Full-Stack Notes App (Django + Nuxt 3)

This is a simple, single-user, full-stack note-taking application built with Django and Nuxt 3. It provides full CRUD (Create, Read, Update, Delete) functionality for notes.

This project was built as a demonstration of core full-stack development skills, integrating a Python/Django backend with a modern JavaScript/Vue frontend.

## Tech Stack

*   **Backend**: Django, Django REST Framework (DRF)
*   **Frontend**: Nuxt 3 (Vue 3), TypeScript
*   **UI**: Tailwind CSS v4, shadcn-vue
*   **Database**: SQLite (default)

## Project Structure

The project is structured as a monorepo with two main directories:

```
/
├── backend/      # Contains the Django REST API
└── frontend/     # Contains the Nuxt 3 frontend application
```

### Getting Started

**Backend Setup:**

1.  Navigate to the `backend` directory: `cd backend`
2.  Create and activate a virtual environment:
    *   `python -m venv venv`
    *   `source venv/bin/activate` (macOS/Linux) or `.\venv\Scripts\activate` (Windows)
3.  Install dependencies: `pip install -r requirements.txt`
4.  Apply database migrations: `python manage.py migrate`
5.  Run the development server: `python manage.py runserver` (available at `http://127.0.0.1:8000`)

#### To run tests:

1.  Ensure you are in the `backend` directory and your virtual environment is activated.
2.  Install the dev dependencies: `pip install -r requirements-dev.txt`
2.  Run the tests: `pytest`

**Frontend Setup:**

1.  Navigate to the `frontend` directory: `cd frontend`
2.  Install dependencies: `npm install`
3.  Run the development server: `npm run dev` (available at `http://localhost:3000`)

---

## Architecture and Key Design Decisions

### 1. Monorepo Structure

I chose a monorepo containing both the `backend` and `frontend` to simplify development and version control, since this is a simple task that does not require complex build processes or deployments. This keeps the API and its consumer in a single repository, making it easier to manage features that span both parts of the stack.

### 2. Backend: Django + DRF

Django was chosen for its robust, "batteries-included" nature, which provides a solid foundation with an ORM, admin panel, and security features out of the box.

**Django REST Framework (DRF)** is the industry standard for building APIs with Django. Its key benefits for this project were:
*   **Rapid Development**: `ModelViewSet` and `ModelSerializer` allowed for the creation of all CRUD endpoints with minimal code.
*   **Browsable API**: The auto-generated browsable API is invaluable for testing the backend endpoints independently of the frontend.
*   **Serialization**: DRF's serializers handle the complex process of converting database models to JSON and validating incoming data.

### 3. Frontend: Nuxt 3

Nuxt 3 was selected as the frontend framework for its powerful features and excellent developer experience:
*   **File-Based Routing**: Simplifies page and route creation immensely.
*   **Server-Side Rendering (SSR)**: Data is fetched on the server initially (`useFetch`), leading to faster perceived page loads and better SEO, as the client receives a fully rendered HTML page.
*   **Auto-Imports**: Components, composables, and utils are automatically imported, leading to cleaner and more concise code.

### 4. UI: Tailwind CSS + shadcn-vue

For the UI, a utility-first approach was chosen with **Tailwind CSS**. This allows for building custom designs rapidly without writing custom CSS files.

**shadcn-vue** was used for UI components (Buttons, Cards, Forms). Unlike other component libraries, `shadcn` is not a dependency. You copy its component code directly into your project, giving you full ownership and control over styling and functionality. This makes it highly customizable and avoids library bloat.

---

## What I'd Improve With More Time

Given more time, I would focus on making the application more robust, feature-rich, and production-ready.

### 1. User Authentication & Authorization

The most critical next step would be to make the app multi-user.
*   **Backend**: Implement JWT (JSON Web Token) authentication using `djangorestframework-simplejwt` or a separate auth service like supabase or Auth0.
*   **Frontend**: Create Login and Register pages. I would use **Pinia** for global state management to store the user's authentication token and profile information, making it accessible across the entire application.

### 2. Enhanced User Feedback & Error Handling

The current error handling is basic. I would improve it by:
*   **Using Toasts/Sonner**: Implement a non-intrusive notification system (e.g., using a "toast" component) to provide feedback for actions like "Note saved successfully" or to display API errors.
*   **Frontend Form Validation**: Add real-time, client-side validation using a library like **Zod** to give users instant feedback on form inputs before they even submit.

### 3. Optimistic UI Updates

To make the application feel instantaneous, I would implement optimistic UI updates. When a user deletes a note, for example, it would be removed from the UI immediately while the API request runs in the background. If the request fails, the UI would revert the change and show an error message.

### 4. Pagination

For applications with many notes, fetching all of them at once is inefficient. I would implement pagination on the backend (DRF has built-in support) and add a "Load More" button or infinite scrolling on the frontend to load notes in batches.

### 5. Comprehensive Testing

*   **Backend**: Write unit tests using `pytest-django` to validate the API logic and models.
*   **Frontend**: Implement component tests with `vitest` to ensure individual UI components work as expected, and end-to-end tests with **Playwright** to simulate user flows through the entire application.

### 6. Containerization

For easier setup and deployment, I would containerize both the frontend and backend services using **Docker** and create a `docker-compose.yml` file to orchestrate the entire application stack.

### 7. Deployment

Finally, I would deploy the application to a cloud provider:
*   **Backend**: Use a service like Heroku, DigitalOcean, or AWS to host the Django API.
*   **Frontend**: Deploy the Nuxt 3 app to Vercel, Netlify or Cloudflare Pages for easy static hosting and CDN distribution. 

### 8. Backend Improvements

*   **API Rate Limiting**: Implement rate limiting to prevent abuse of the API.
*   **Logging and Monitoring**: Set up logging (using Django's built-in logging or a service like Sentry) to monitor errors and performance issues in production.
*   **CORS Configuration**: Ensure proper CORS settings to allow the frontend to communicate with the backend securely.

## What AI tools did I use?

I used Gemini 2.5 pro to help mostly with the initial code generation and structuring (specially for the frontend). I also used it to help with the README file and some of the explanations. It had some trouble with the frontend setup, so I had to do it myself with the help of the Nuxt3 documentation. It also helped with the setup for the unit tests on the backend.