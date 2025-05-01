# 👨‍🍳 Cook Inventory

Cook inventory is a simple and intuitive full stack app made for help kitchens manage their inventory resources 

⸻

## ⚙️ Tech Stack

| Layer      | Tech                              |
|------------|-----------------------------------|
| Backend    | Flask, SQLAlchemy                 |
| Frontend   | Jinja2, HTML, CSS, Bootstrap and Javascript |
| Database   | Supabase (Database and File Storage)    |
| DevOps  | Docker |

⸻

## 🚀 Features
- 🔒 Session-based authentication
- 💻 Simple and intuitive UI
- 🔰 Category management for the inventory items
- 📝 Inventory management with highlighting of items that need replenishment
- 🐳 Dockerized development environment
⸻

## 📂 Project Structure

<pre>

```
cook-inventory
├── src/
│   ├── app/            # Flask APP
│   │   ├── auth/       # Auth features module
│   │   ├── category/   # Category features Module 
│   │   ├── inventory/  # Inventory features module
│   │   └── user/       # User features module
│   ├── migrations/     # DB migrations
│   ├── static/         # Static Files like Images
│   └── templates/      # Global Templates Files
│
├── .github/            # Assets
├── .env.exemple        # Env Variables Exemple
├── docker-compose.yml			
└── README.md
```
</pre>

⸻

## 🚀 Getting Started

### 📦 Requirements
	•	Docker & Docker Compose
	•	Python 3.12+

⸻

## 🐳 Start with Docker

### Build and run everything

`docker-compose up --build`

Access the full stack app at http://localhost:5000

⸻

## 🪟 Demonstration

### Auth Features

> Login

[login](./.github/assets/videos/login-page.webm)

### Category Management Features

> Category CRUD

[category_crud](./.github/assets/videos/category-crud.webm)

> Category has Inventory Items and Cant be Deleted

[category_cant_delete](./.github/assets/videos/category-cant-delete.webm)

### Inventory Management Features

> Inventory CRUD

[inventory_crud](./.github/assets/videos/inventory-crud.webm)
[inventory_crud_delete](./.github/assets/videos/inventory-delete-item.webm)

<!-- ## 🧪 Run Tests

Backend tests (pytest):

cd backend
pytest

Frontend lint:

cd frontend
npm install
npm run lint


⸻

## 🧹 Pre-commit Hooks

### One-time setup
pre-commit install

### Run all hooks manually
pre-commit run --all-files

That’s looking super clean and professional, Leo! 🔥 Here’s the final section you can append to your README.md:

⸻

## 🧭 Next Steps
Check out the [Project board]() to see what’s coming next!
We’re actively working on new features like:
- User profile pages
- OAuth login
- Admin dashboard
- Genre-based book filters
- More AI enhancements

Stay tuned and feel free to contribute! -->