# 👨‍🍳 Cook Inventory

Cook inventory is a simple and intuitive full stack app made for help kitchens manage their inventory resources 

⸻

## ⚙️ Tech Stack

| Layer      | Tech                              |
|------------|-----------------------------------|
| Backend    | Flask, SQLAlchemy                 |
| Frontend   | Jinja2, HTML, CSS, Bootstrap and Javascript |
| Database   | PostgreSQL, Supabase (File Storage)   |
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

## 🪟 Demonstration

### Auth Features

> Login

[login-page.webm](https://github.com/user-attachments/assets/ff02f986-c5b3-4b95-b628-058f723c580a)

### Category Management Features

> Category CRUD

[category-crud.webm](https://github.com/user-attachments/assets/170e6fe2-511f-4863-a195-313f9e1a377a)

> Category has Inventory Items and Cant be Deleted

[category-cant-delete.webm](https://github.com/user-attachments/assets/65112080-7251-48f4-b140-00d98efe252d)

### Inventory Management Features

> Inventory CRUD

[inventory-crud.webm](https://github.com/user-attachments/assets/4c2c63c0-83ad-48d9-8d95-83ff1a9aad8f)

[inventory-delete-item.webm](https://github.com/user-attachments/assets/67d0e8d7-147a-4576-a22b-2b77817a3a94)

⸻

## 🚀 Getting Started

### 📦 Requirements
	• Python 3.12+
	• Supabase Account
	• Docker & Docker Compose

⸻

## 🐳 Start with Docker

### Setup Env Variables

1. Put any key in `TOKEN_SECRET` variable (I recomend you execute the follow command to generate your secret: `openssl rand -hex 32`)
2. Sign-up in [Supabase](https://supabase.io/), create an project and setup your database password
3. Go to "Project Settings > Data API" copy the Project URL" and put in `SUPABASE_URL` variable
4. Go to "Project Settings > Data API" copy the public project API Key and put in `SUPABASE_KEY` variable
5. Click in "Connect" button in the project dashboard, copy the connection string, replace your password and put that value in `SQLALCHEMY_DATABASE_URI`

OBS: You can use other database if you want, but you need the supabase to upload the images.

Once you do that steps, you can run with the docker following the steps below.

### Build and run everything

`docker-compose up --build`

Access the full stack app at http://localhost:5000

⸻

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
