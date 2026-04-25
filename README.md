# School Database API (DRF Project)

This repository is a hands-on Django REST Framework (DRF) learning project.

The goal of this project is to implement and demonstrate DRF concepts I learned, including serializers, function-based APIs, class-based generic APIs, viewsets, pagination, filtering, status codes, and model relationships.

## Project Purpose

This project is not focused on production architecture. It is built to practice DRF concepts in a practical way across multiple apps:
- `students`
- `professors`
- `result`
- `library`

## DRF Concepts Implemented

### 1. ModelSerializer
- Implemented in multiple apps to convert model instances into JSON and validate incoming request data.
- Examples:
  - `students/serializers.py`
  - `professors/serializers.py`
  - `library/serializers.py`

### 2. Function-Based API Views (`@api_view`)
- Used in `students/views.py` for explicit request-method handling.
- Demonstrates manual control of GET/POST/PUT/DELETE logic.

### 3. Generic Class-Based Views
- Used in `result/views.py` and `library/views.py`.
- Implemented classes:
  - `ListCreateAPIView`
  - `RetrieveUpdateDestroyAPIView`
- Shows cleaner CRUD implementation with less boilerplate.

### 4. ViewSets + Router
- `professors/views.py` uses `ModelViewSet`.
- `_school_project_root/urls.py` uses `DefaultRouter` to auto-generate professor endpoints.
- This demonstrates DRF routing and standard REST endpoint generation.

### 5. Pagination
- Global DRF pagination configured in `_school_project_root/settings.py` (`LimitOffsetPagination`).
- Custom pagination class implemented in `_school_project_root/pagination.py` (`MyPagination` based on `PageNumberPagination`).
- `ProfessorViewSet` applies the custom pagination class.

### 6. Filtering (`django-filter`)
- Global filter backend enabled in settings.
- Field-based filtering implemented in `ProfessorViewSet` with:
  - `filter_backends = [DjangoFilterBackend]`
  - `filterset_fields = ['degree', 'id']`

### 7. Nested Serialization / Related Data Representation
- Demonstrated in:
  - `library/serializers.py` (Author with nested books)
  - `result/serializers.py` (Result with nested marksheet)
- Also includes `PrimaryKeyRelatedField` + `source` pattern for write-only relation input in `MarkSheetSerializer`.

### 8. HTTP Status Codes and Validation Flow
- Explicit status codes are returned in API responses (`200`, `201`, `204`, `400`, `404`) across views.
- Serializer `.is_valid()` and `.errors` flow is implemented for request validation.

### 9. URL Routing with App Separation
- Central URL configuration in `_school_project_root/urls.py`.
- App-level URL files used where appropriate (`students/urls.py`, `library/urls.py`).

### 10. SQLite + Migrations
- Uses SQLite (`db.sqlite3`) for local learning and quick setup.
- App-specific migrations are included to track model changes.

## Quick Start (Run Only)

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd school\ database
```

### 2. Install dependencies
This project uses Pipenv.

```bash
pipenv install
```

### 3. Activate shell
```bash
pipenv shell
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Run the server
```bash
python manage.py runserver
```

### 6. Open in browser
- Home: `http://127.0.0.1:8000/`
- Students: `http://127.0.0.1:8000/students/studentlist/`
- Professors (router): `http://127.0.0.1:8000/professors/`
- Result: `http://127.0.0.1:8000/result/`
- Marksheet: `http://127.0.0.1:8000/marksheet/`
- Library author: `http://127.0.0.1:8000/library/author/`
- Library books: `http://127.0.0.1:8000/library/books/`

## Notes
- This repository is intentionally built as a DRF concept-practice project.
- It focuses on learning and implementation clarity over production hardening.
