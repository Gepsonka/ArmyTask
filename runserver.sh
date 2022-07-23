echo "If you leave the port empty it will automatically be 8000."
read -p "Port: " port 

python3 CarDatabase/manage.py runserver $port