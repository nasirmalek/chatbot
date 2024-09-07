from django_chatbot.settings import GOOGLE_API_KEY
def get_api_key(request):
    return {'GOOGLE_API_KEY':GOOGLE_API_KEY}