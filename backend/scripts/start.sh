#!/bin/sh

python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate --no-input
python manage.py collectstatic --no-input --clear
echo "from auth_custom.models import User; User.objects.create_superuser('$ADMIN_USER', '$ADMIN_MAIL', '$ADMIN_PASSWORD', first_name='$ADMIN_FIRST_NAME', last_name='$ADMIN_LAST_NAME')" | python3 manage.py shell
python manage.py runserver 0.0.0.0:8000