Instructions to setup the environment

1. install python, add it to the environment path
2. install vscode
3. setting up the virtual environment
    a) open cmd
    b) execute "pip install virtualenvwrapper-win" without quotes
    c) mkvirtualenv "somename"  eg. mkvirtualenv test
4. open vscode
    a) install jinja, python extensions
    b) open project folder in vscode (ctrl + K, ctrl + O)
    c) open terminal (ctrl + `)
    d) now type "workon 'virtualenv name'" without quotes  eg. workon test ; (everytime you restart the terminal, you need to execute this)
    e) type "pip install django djangorestframework django_tables2" without quotes
    f) execute "python manage.py makemigrations"
    g) execute "python manage.py migrate"
    h) execute "python manage.py runserver"

(OPTIONAL Configuration)

1. install postgresql, pgadmin4
2. run pgadmin4
3. create a database or use the default one
4. goto big/settings.py in the project folder and edit the DATABASES dictionary to below settings
    DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'someother',
          'USER': 'postgres',
          'PASSWORD': '',
          'HOST': 'localhost'
      }
    }
5. change the NAME field to the newly created database name and PASSWORD field to the postgres password given while installing in the above configuration
6. now run commands from 4f, 4g, 4h

