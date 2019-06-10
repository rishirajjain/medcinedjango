# medicine search engine

#Open settings.py from meds folder, look for databases section and change the password for mysql in your computer.
#check if this database is available in mysql in your computer named 'drgipatel_bor1'.

Open up a fresh terminal, navigate to where you have the elasticsearch-5.6.8 then run the command ./elasticsearch inside bin folder(check screenshots).

In another terminal window do:
You can do the following commands after you enable your (venv)(check screenshots from other day).
If every thing looks smooth till here then run;
1.  'python manage.py makemigrations'
2.  'python manage.py migrate'
3.  'python manage.py search_index --rebuild'
4.  'python manage.py runserver'

This should give you no errors if it ran successfully.
and localhost should be up and running on http://localhost:8000/


navigate to :http://localhost:8000/search/
and test out the searching!

