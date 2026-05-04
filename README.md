# 🚀 Django Starter Template

A clean and modern Django starter setup with an optimized development workflow.

---

## ⚙️ Features

- 🧠 Clean project structure (app-based templates)
- 🎨 Tailwind CSS autocomplete support in templates
- 🧩 Django template inheritance setup
- 🔥 Template formatting via **djLint**
- 🐍 Python formatting via **Black + isort**
- ⚡ Enhanced development tools via **django-extensions**
- 🧪 Improved debugging (`runserver_plus`, `shell_plus`)

---

## 📂 Project Structure

```
project/
├── base/                  # Main app
│   ├── templates/
│   │   └── base/
│   │       ├── base.html
│   │       └── index.html
│   ├── templatetags/
│   └── views.py
├── project/               # Django config
├── manage.py
```

---

## 🛠️ Installation

### 1. Clone the repo

```
git clone https://github.com/code-kasha/starter-django
cd starter-django
```

---

### 2. Create virtual environment

```
python -m venv .env
# Mac/Linux : source .env/bin/activate
# Windows   : .env\Scripts\activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## 🚀 Run Development Server

```
python manage.py runserver
```

---

## 🔧 Useful Commands

### Enhanced Django shell

```
python manage.py shell_plus
```

### Better dev server (debugging)

```
python manage.py runserver_plus
```

### Generate model graph

```
python manage.py graph_models -a -o schema.png
```

---

## 🧠 Formatting Setup

| Type             | Tool          |
| ---------------- | ------------- |
| Python           | Black + isort |
| Django Templates | djLint        |

---

## ⚠️ Notes

- Prettier does not support Django templates → handled via **djLint**
- Template inheritance requires correct paths (e.g. `"base/base.html"`)

---

## 📌 Future Improvements

- [ ] Authentication system
- [ ] API integration (Django REST Framework)
- [ ] Docker setup
- [ ] Production deployment

---

## 👨‍💻 Author

Akash Damle
