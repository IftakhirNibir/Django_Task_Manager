# Project Name: Task Manager
The application should allow multiple users to create, view, update, and delete tasks.

## The way to set up and run the project.
1. First, you need to install Python and pip on your local machine
2. Create a folder and open the terminal in that folder
3. Create a virtual environment using the terminal. For example, the environment name is "env"
```bash
python -m venv env 
```
4. Activate the environment
```bash
env\Scripts\activate
```
5. Now you need to clone the repository.
```bash
git clone https://github.com/IftakhirNibir/Django_Task_Manager.git 
```
6. Open the project folder
```bash
cd Django_Task_Manager
```
7. Install the required prerequisites using
```bash
pip install -r requirement.txt
```
8. Open "task_manager" folder
```bash
cd task_manager
```
9. Create ".env" file inside the current folder
10. Now copy the below section and paste it into your ".env" file and make the necessary changes
```bash
DB_ENGINE=django.db.backends.postgresql
DB_NAME=<Your-DB-Name>
DB_USER=<Your-DB-UserName>
DB_PASSWORD=<Your-DB-Password>
DB_HOST=<Your-DB-Host>
DB_PORT=<Your-DB-PortNumber>
```
11. Now run the server
```bash
py manage.py runserver
```
12. Open the browser and go 
```bash
http://127.0.0.1:8000/
```
Now you need to sign up and log in to get our service
13. You can also visit our admin panel. For this, you need to create superuser in terminal
```bash
py manage.py createsuperuser
```
