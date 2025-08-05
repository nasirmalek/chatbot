# Django Chatbot

A Django-based chatbot application powered by Google's Generative AI (Gemini). This application provides a web interface for users to interact with an AI chatbot with user authentication and chat history.

## Features

- 🤖 AI-powered chatbot using Google Gemini
- 👤 User authentication (login/register)
- 💬 Chat history storage
- 🔒 Secure session management
- 📱 Responsive web interface
- 🚀 Production-ready deployment configurations

## Quick Start

### 1. Clone the Repository
```bash
git clone <repository-url>
cd chatbot
```

### 2. Environment Setup
```bash
# Copy environment template
cp .env.example .env

# Edit .env with your configuration
nano .env
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Edit `.env` file:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
GOOGLE_API_KEY=your-google-api-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Run Database Migrations
```bash
python manage.py migrate
```

### 6. Start the Application
```bash
python manage.py runserver
```

Visit http://localhost:8000 to access the application.

## Deployment

This application is ready for production deployment. See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

### Quick Deployment Options:

**Docker:**
```bash
docker build -t chatbot .
docker run -p 8000:8000 --env-file .env chatbot
```

**Heroku:**
```bash
heroku create your-app-name
heroku config:set GOOGLE_API_KEY=your-key-here
git push heroku main
```

**Local Production:**
```bash
./deploy.sh
gunicorn django_chatbot.wsgi:application
```

## Configuration

### Required Environment Variables

| Variable | Description |
|----------|-------------|
| `GOOGLE_API_KEY` | Google AI API key for Gemini |
| `SECRET_KEY` | Django secret key |
| `DEBUG` | Debug mode (True/False) |
| `ALLOWED_HOSTS` | Comma-separated allowed hosts |

### Optional Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DATABASE_URL` | SQLite | Database connection URL |
| `STATIC_ROOT` | staticfiles | Static files directory |

## Project Structure

```
chatbot/
├── chatbot/                 # Main Django app
│   ├── models.py           # Database models
│   ├── views.py            # Application views
│   ├── urls.py             # URL routing
│   └── management/         # Custom management commands
├── django_chatbot/         # Django project settings
│   ├── settings.py         # Main settings
│   ├── urls.py            # Root URL configuration
│   └── wsgi.py            # WSGI application
├── templates/              # HTML templates
├── static/                 # Static files
├── staticfiles/           # Collected static files
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose setup
├── Procfile             # Heroku configuration
├── vercel.json          # Vercel deployment
└── deploy.sh            # Deployment script
```

## API Integration

This application uses Google's Generative AI (Gemini Pro) for chat responses. To get an API key:

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add it to your `.env` file as `GOOGLE_API_KEY`

## Security

- User authentication required for chatbot access
- CSRF protection enabled
- Secure session management
- Environment-based configuration
- Production security headers

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For deployment issues, see [DEPLOYMENT.md](DEPLOYMENT.md)
For application issues, check the logs and environment configuration.

---

**Ready for deployment!** 🚀