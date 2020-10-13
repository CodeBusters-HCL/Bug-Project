<h2>Instructions to setup the environment</h2>

1. install <a href="https://www.python.org/downloads/" style="text-decoration: none">python</a>, add it to the environment path<br>
2. install <a href="https://code.visualstudio.com/download" style="text-decoration: none">vscode</a><br>
3. setting up the virtual environment
    a) 
4. open vscode<br>
    a) install jinja, python extensions<br>
    b) open project folder in vscode (ctrl + K, ctrl + O)<br>
    c) open terminal (ctrl + `)<br>
    d) 
    e) now install required python packages <pre>pip install django djangorestframework django_tables2</pre>
    f) now run the commands 
    <pre>
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    </pre>
 
<h2>(OPTIONAL Configuration)</h2>
<h4>Setting up virtual environment</h4>
1. setting up the virtual environment  (optional, if using builtin environmet)<br>
    a) open cmd<br>
    b) execute <pre>pip install virtualenvwrapper-win</pre>
    c) mkvirtualenv "somename"  <pre>eg. mkvirtualenv test</pre>
    d) now type "workon 'virtualenv name'" without quotes; (optional if using builtin environment)(everytime you restart the terminal, you need to execute this) <pre>eg. workon test</pre>
<h4>Setting up the custom sql database</h4>
2. install <a href="https://www.postgresql.org/download/" style="text-decoration: none">postgresql</a>, <a href="https://www.pgadmin.org/download/" style="text-decoration: none">pgadmin4</a><br>
3. run pgadmin4<br>
4. create a database or use the default one<br>
5. install psycopg2 <pre>pip install psycopg2</pre>
6. goto big/settings.py in the project folder and edit the DATABASES dictionary to below settings<br>
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
7. change the NAME field to the newly created database name and PASSWORD field to the postgres password given while installing in the       &nbsp;above configuration<br>
8. now run commands
<pre>
 python manage.py makemigrations
 python manage.py migrate
 python manage.py runserver
</pre>
