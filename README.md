# Desafio
  Installation Instructions

    1. Install the Requirements
      pip install -r requirements.txt
    
    2. Sync the DB

        create schema "database" in mySQL
        run commands: python manage.py migrate syncdb
        
        run populate.py from the project to populate "restapi_music" table with information
    
    3. Run the server
        python manage.py runserver
