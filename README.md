<h2>Instructions to setup the environment</h2>

1. install python, add it to the environment path<br>
2. install vscode<br>
3. setting up the virtual environment<br>
    a) open cmd<br>
    b) execute <pre>pip install virtualenvwrapper-win</pre>
    c) mkvirtualenv "somename"  <pre>eg. mkvirtualenv test</pre>
4. open vscode<br>
    a) install jinja, python extensions<br>
    b) open project folder in vscode (ctrl + K, ctrl + O)<br>
    c) open terminal (ctrl + `)<br>
    d) now type "workon 'virtualenv name'" without quotes;  (everytime you restart the terminal, you need to execute this) <pre>eg. workon test</pre>
    e) now install required python packages <pre>pip install django djangorestframework django_tables2</pre>
    f) now run the commands <pre>python manage.py makemigrations</pre><pre>python manage.py migrate</pre><pre>python manage.py migrate</pre><pre>python manage.py runserver</pre>
 
<h2>(OPTIONAL Configuration)</h2>

1. install postgresql, pgadmin4<br>
2. run pgadmin4<br>
3. create a database or use the default one<br>
4. goto big/settings.py in the project folder and edit the DATABASES dictionary to below settings<br>
<pre>
    DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'someother',
          'USER': 'postgres',
          'PASSWORD': '',
          'HOST': 'localhost'
      }
    }
</pre>
5. change the NAME field to the newly created database name and PASSWORD field to the postgres password given while installing in the       &nbsp;above configuration<br>
6. now run commands
<pre>
 python manage.py makemigrations
 python manage.py migrate
 python manage.py runserver
</pre>

