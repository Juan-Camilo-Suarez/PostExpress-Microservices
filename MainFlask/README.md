create file migrations = flask db init
make a migration = flask db migrate
migrate = flask db upgrade

# MainFlask

## 1. Installing and running the project

### 1.1 Form

1. Create a virtual environment:\
   ```python -m venv venv```
2. Activate virtual environment:\
   ```venv\Scripts\activate.bat``` - для Windows \
   ```source venv/bin/activate``` - для Linux и MacOS
3. Install dependencies:\
   ```pip install -r requirements.txt ```
4. Install MYSQL from Docker:\
   ``` docker-compose up -d db  ```
5. Create file migrations :\
   ```flask db init```
6. Make a migration to database:\
   ```flask db migrate```
7. Apply migrations to database:\
   ```flask db upgrade```
8. Server start:\
   ```python main.py```

### 1.2 Form with Docker-compose

1. Install MYSQL from Docker:\
   ``` docker-compose up -d db  ```
2. Execute Docker-Compose:\
   ``` MainFlask/docker-compose up```
3. Open docker-compose console:\
   ```docker-compose exec backend sh ```
4. Create file migrations (in this case this step you can ignore ) :\
   ```flask db init```
5. Make a migration to database:\
   ```flask db migrate```
6. Apply migrations to database:\
   ```flask db upgrade```
7. Server start:\
   ```python main.py```
