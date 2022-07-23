#!/bin/bash

echo "================================================"
echo "Django Car database apllication by Botond Molnar"
echo "================================================"
echo "Version: 1.0.0-RELEASE"
echo "======================"

echo "==============================="
echo "Installing python virtualenv..."
echo "==============================="

if python3 -m pip install virtualenv; then
    echo "python3 virtualenv was successfully created"
else 
    echo "Could not install python3 virtualenv :("
    echo "Check if the script has correct rights and you have internet connection."
    exit 0
fi

if python3 -m venv ./venv; then
    echo "Venv was created successfully"
else 
    echo "Could not create venv :("
    exit 0
fi

current_dir=`pwd`
venv_path="/venv/bin/activate"

if source $current_dir$venv_path; then
    echo "venv started successfully"
else 
    echo "Could not start venv :("
    exit 0
fi


echo "=========================="
echo "Installing dependencies..."
echo "=========================="

if python3 -m pip install -r requirements.txt; then
    echo "Dependencies are installed."
else 
    echo "Could not install dependencies :("
    exit 0
fi

echo "====================="
echo "Creating .env file..."
echo "====================="

echo "DJANGO_SECRET=-7huzqi_15%d3t+oprzw0%bdh\$!x&lnad2u6(ac27jx4a*#sp%" > ./CarDatabase/.env


echo "====================="
echo "Migrating database..."
echo "====================="

if python3 $current_dir/CarDatabase/manage.py makemigrations; then
    echo "Migration files created successfully!"
else 
    echo "Could not create migration files"
    exit 0
fi


if python3 $current_dir/CarDatabase/manage.py migrate; then
    echo "Successfully migrated database!"
else 
    echo "Could not migrate databse :("
    exit 0
fi

echo "====================="
echo "Creating superuser..."
echo "====================="

read -p 'Username: ' uservar
read -sp 'Password: ' passwdvar

cd CarDatabase
read -d '' python_cmd << EOF
from CustomUser.models import CustomUser
CustomUser.objects.create_superuser(
    username = '$uservar',
    email = 'a@b.com',
    password = '$passwdvar',    
).save()
EOF

if python3 manage.py shell -c "$python_cmd"; then
    echo ""
else
    echo "Could not create superuser :("
    exit 0
fi

echo "==================================="
echo "Superuser was successfully created!"
echo "==================================="
echo ""
echo ""

echo "Install process finished. The first thing you should do"
echo "is changing DJANGO_SECRET in the .env file in the CarDatabase folder."
echo "You can generate django secret on this site:"
echo "https://djecrety.ir/"
echo "===================================================================="
echo "you can start the server with the runserver.sh script"

echo "Have fun examining the application :D!"