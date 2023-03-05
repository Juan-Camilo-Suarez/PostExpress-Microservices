# DjangoAdmin

## 1.  Installing and running the project
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
5. Apply migrations to database:\
```python src/manage.py migrate```
6. Server start:\
```python src/manage.py runserver```

### 1.2 Form with Docker-compose
1. Execute Docker-Compose:\
``` DjangoAdmin/docker-compose up```

