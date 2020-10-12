<h2>Instructions to setup the environment</h2>

1. install python, add it to the environment path<br>
2. install vscode<br>
3. setting up the virtual environment<br>
    a) open cmd<br>
    b) execute "pip install virtualenvwrapper-win" without quotes<br>
    c) mkvirtualenv "somename"  eg. mkvirtualenv test<br>
4. open vscode<br>
    a) install jinja, python extensions<br>
    b) open project folder in vscode (ctrl + K, ctrl + O)<br>
    c) open terminal (ctrl + `)<br>
    d) now type "workon 'virtualenv name'" without quotes  eg. workon test ; (everytime you restart the terminal, you need to execute this)<br>
    e) type "pip install django djangorestframework django_tables2" without quotes<br>
    f) execute "python manage.py makemigrations"<br>
    g) execute "python manage.py migrate"<br>
    h) execute "python manage.py runserver"<br>

(OPTIONAL Configuration)

A). install postgresql, pgadmin4<br>
B) run pgadmin4<br>
C) create a database or use the default one<br>
D) goto big/settings.py in the project folder and edit the DATABASES dictionary to below settings<br>
    DATABASES = {<br>
      'default': {<br>
          'ENGINE': 'django.db.backends.postgresql',<br>
          'NAME': 'someother',<br>
          'USER': 'postgres',<br>
          'PASSWORD': '',<br>
          'HOST': 'localhost'<br>
      }<br>
    }<br>
E) change the NAME field to the newly created database name and PASSWORD field to the postgres password given while installing in the above configuration<br>
F) now run commands from 4f, 4g, 4h<br>

