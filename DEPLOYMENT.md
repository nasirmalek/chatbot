# Django Chatbot Deployment Guide

This guide explains how to deploy the Django Chatbot application using various deployment methods.

## Prerequisites

1. Python 3.12+
2. Git
3. Google API Key for Generative AI

## Environment Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd chatbot
   ```

2. **Create environment configuration:**
   ```bash
   cp .env.example .env
   ```

3. **Edit `.env` file with your configuration:**
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=False
   ALLOWED_HOSTS=your-domain.com,localhost
   GOOGLE_API_KEY=your-google-api-key-here
   ```

## Local Development

1. **Run the deployment script:**
   ```bash
   ./deploy.sh
   ```

2. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

3. **Access the application:**
   - Open http://localhost:8000 in your browser

## Production Deployment

### Option 1: Docker Deployment

1. **Build and run with Docker:**
   ```bash
   docker build -t django-chatbot .
   docker run -p 8000:8000 --env-file .env django-chatbot
   ```

2. **Or use Docker Compose:**
   ```bash
   docker-compose up -d
   ```

### Option 2: Heroku Deployment

1. **Install Heroku CLI and login:**
   ```bash
   heroku login
   ```

2. **Create a new Heroku app:**
   ```bash
   heroku create your-chatbot-app-name
   ```

3. **Set environment variables:**
   ```bash
   heroku config:set SECRET_KEY=your-secret-key-here
   heroku config:set GOOGLE_API_KEY=your-google-api-key-here
   heroku config:set DEBUG=False
   ```

4. **Deploy to Heroku:**
   ```bash
   git push heroku main
   ```

### Option 3: VPS/Server Deployment

1. **On your server, clone the repository:**
   ```bash
   git clone <repository-url>
   cd chatbot
   ```

2. **Run deployment script:**
   ```bash
   ./deploy.sh
   ```

3. **Start with Gunicorn:**
   ```bash
   gunicorn django_chatbot.wsgi:application --bind 0.0.0.0:8000
   ```

4. **Configure reverse proxy (Nginx example):**
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }

       location /static/ {
           alias /path/to/your/app/staticfiles/;
       }
   }
   ```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | Development key |
| `DEBUG` | Django debug mode | True |
| `ALLOWED_HOSTS` | Allowed hosts | localhost,127.0.0.1 |
| `GOOGLE_API_KEY` | Google AI API key | Required |
| `DATABASE_URL` | Database URL | SQLite |
| `STATIC_ROOT` | Static files root | staticfiles |

## Security Considerations

1. **Never commit `.env` file to version control**
2. **Use strong SECRET_KEY in production**
3. **Set DEBUG=False in production**
4. **Configure proper ALLOWED_HOSTS**
5. **Use HTTPS in production**
6. **Secure your Google API key**

## Database Setup

The application uses SQLite by default. For production, consider:

1. **PostgreSQL (recommended):**
   ```
   DATABASE_URL=postgres://user:password@host:port/database
   ```

2. **MySQL:**
   ```
   DATABASE_URL=mysql://user:password@host:port/database
   ```

## Static Files

Static files are handled by WhiteNoise middleware for simple deployments. For high-traffic applications, consider using a CDN or separate static file server.

## Monitoring and Logs

1. **View application logs:**
   ```bash
   # Local
   python manage.py runserver --verbosity=2

   # Heroku
   heroku logs --tail

   # Docker
   docker logs container-name
   ```

2. **Health check endpoint:**
   - The application includes basic health monitoring
   - Monitor `/admin/` for admin access

## Troubleshooting

### Common Issues:

1. **GOOGLE_API_KEY not set:**
   - Ensure the environment variable is properly configured
   - Check if the API key has proper permissions

2. **Static files not loading:**
   - Run `python manage.py collectstatic`
   - Check STATIC_ROOT configuration

3. **Database migrations:**
   - Run `python manage.py migrate`
   - Check database permissions

4. **Permission errors:**
   - Ensure proper file permissions
   - Check if user has write access to required directories

## Support

For issues and questions:
1. Check the application logs
2. Verify environment configuration
3. Ensure all dependencies are installed
4. Check firewall and network settings