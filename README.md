# CV Generator 📄

A modern, full-stack **Django** web application for creating, previewing, and downloading professional resumes as beautifully formatted PDFs.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.1-092E20?logo=django&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- **Create Profiles** — Fill in a clean, sectioned form with personal info, education, work experience, and skills
- **Dashboard** — View all saved profiles in an elegant card grid with avatar initials and quick actions
- **Resume Preview** — View a polished, document-style resume with gradient header, education cards, and interactive skill chips
- **PDF Download** — Generate and download a print-ready A4 PDF resume in one click (powered by `xhtml2pdf`)
- **Modern Dark UI** — Glassmorphism nav, animated gradient mesh background, smooth micro-animations, and responsive layouts
- **Mobile Friendly** — Fully responsive design that works on all screen sizes

---

## 🖼️ Pages

| Page | URL | Description |
|------|-----|-------------|
| Dashboard | `/` | Hero section + profile card grid |
| Create CV | `/saveprofile/` | Multi-section profile creation form |
| Resume Preview | `/<id>/` | Beautiful interactive resume view |
| Download PDF | `/download/<id>/` | Generates and downloads a PDF resume |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- pip

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/cv-generator.git
cd cv-generator/mysite
```

### 2. Create a virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser.

---

## 📁 Project Structure

```
mysite/
├── manage.py
├── requirements.txt
├── .gitignore
├── README.md
├── mysite/                  # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── myapp/                   # Main application
    ├── models.py            # Profile model
    ├── views.py             # Dashboard, form, preview, PDF views
    ├── urls.py              # URL routing
    └── templates/myapp/
        ├── base.html            # Shared layout (nav, footer, design system)
        ├── dashboard.html       # Profile listing with card grid
        ├── accept.html          # Profile creation form
        ├── resume.html          # Interactive resume preview
        └── download_resume.html # PDF-optimized template for xhtml2pdf
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django 6.1 |
| Database | SQLite (default) |
| PDF Generation | xhtml2pdf |
| Frontend | HTML5, CSS3, JavaScript |
| Typography | Google Fonts (Inter) |
| Design | Dark mode, glassmorphism, CSS animations |

---

## 📝 Model

The `Profile` model stores all CV data:

| Field | Type | Description |
|-------|------|-------------|
| `name` | CharField | Full name |
| `email` | EmailField | Email address (unique) |
| `phone` | CharField | Phone number |
| `degree` | CharField | Degree / qualification |
| `school` | CharField | School name |
| `university` | CharField | University name |
| `summary` | TextField | Professional summary |
| `previous_work` | TextField | Work experience (one entry per line) |
| `skills` | CharField | Comma-separated skills |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
