import os
import threading
import webbrowser
from django.core.management import call_command

def run_server():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm.settings')
    call_command('runserver', '127.0.0.1:8000')

threading.Thread(target=run_server).start()
webbrowser.open("http://127.0.0.1:8000")


    
