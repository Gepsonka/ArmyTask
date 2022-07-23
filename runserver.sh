echo "If you do not give port it will be automatically 8000: "
read -p "Port" port 

python3 CarDatabase/manage.py runserver $port