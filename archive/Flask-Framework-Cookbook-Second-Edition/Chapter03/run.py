from my_app import app, manager, db


# app.run()


manager.run()



# Useing flask-migrate
# 1. Settup flask_migrate and flask_script in app file. 
# 2. Import manager to run file 
# 3. Switch to pipenv shell (only need it if pipenv i.e  pipfile and pipfile.lock are not in app folder)
# 4. Cd to run file if your not 
# 5. > pipenv run python run.py db init  or if in shell > python run.py db init
# 6. > python run.py db migrate
# 7. > python run.py db upgrade    or     downgrade
# 8. > python run.py runserver