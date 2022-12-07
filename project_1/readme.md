## Rota planning app for use in the Bell Jar

![Screenshot of landing page of the Bell Jar](https://memimemimemi.neocities.org/imagehosting/Screenshot%202022-12-07%20at%2012.04.34.png)

## BRIEF:

Build an app that lets you write rotas for employee shifts in the Bell Jar (a pub with a small pool of staff in the Southside of Glasgow). It should automate some of the more tedious processes of putting together a weekly rota, and make aspects of the task easier than they currently are. The owner/manager of the pub (Steve) should be able to create, edit and delete Rotas and Staff, while the Staff can view their shifts for the week as well as the full rota.

### MVP:
* The app should allow Steve (the owner of the pub) to create, edit and remove staff members
* Staff members should be able to edit their profiles on the app to indicate the maximum and minimum amount of hours that they would like to work
* The app should also allow Steve to write a rota for the week, with the information about staff hours displayed so that he can write a rota that satisfies as many staff members as possible
* The staff should be able to view the rota in full, or by staff member, or by day.

### Possible Extensions:
* Steve should be able to write notes about various days—e.g. "on Sunday there is a function and that there will be one extra member of staff", or "Friday closed for Christmas"
* Allow staff members to request to swap shifts with other staff members
* Allow staff members to call in sick for shifts, and for that to be reflected in the rota
* Allow the create/edit rota screens to display whether the current configuration is satisfying the staff availability and hours needs
* Create an auto-write function that randomly allocates staff only to shifts that they are available to do, without rotaing staff in for too many or too few hours
* Create a template for the rota that indicates whether more or less staff are needed on specific days, and whether certain gshifts need to be covered or not.
* Create a function that allows you to recall previous week's rotas as a starting point for writing the next week's one

## RUNNING INSTRUCTIONS:

* Clone the github repository
* Install flask, psycopg3, PostgreSQL, and python3
* Create a database called "belljar_admin"
* In the terminal, from the directory "belljar_rota" run the command "psql -d belljar_admin -f db/belljar_admin.sql"
* From the same directory, run the command "python3 console.py"
* Now enter the command "flask run"
* Navigate to your browser of choice (The create rota features work quickest in Safari but have also been tested in Chrome) and enter in the url "http://127.0.0.1:4999"
* Congratulations! In only 7 simple steps with only 4 different installations, you are now writing the rota for the Bell Jar