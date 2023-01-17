# vidita-systems-assignment

### Frontend
Setup frontend:
```
cd frontend
npm init
```

Start frontend:
```
npm run dev
```

### Backend
Setup backend:
```
cd assignment
python3 -m venv venv
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
```

Start backend:
```
python3 manage.py runserver      
```