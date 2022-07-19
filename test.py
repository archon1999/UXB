import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from backend.models import User

user = User.users.get(email='ibadullaev.kamoladdin1973@gmail.com')
subject = 'Saytdan ro`yhatdan o`tish'
message = f'Kalit: {user.key}'
user.email_user(subject, message)
