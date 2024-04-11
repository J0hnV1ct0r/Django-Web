class DataBase:
    def __init__(self, engine='django.db.backends.sqlite3', name='db.sqlite3'):
        self.engine = engine
        self.name = name
