from flask_login import UserMixin
import sqlite3
import time
from config import Config


def get_db_connection():
    retries = 5
    while retries > 0:
        try:
            conn = sqlite3.connect(Config.USER_DATABASE_PATH)
            return conn
        except sqlite3.OperationalError as e:
            if 'database is locked' in str(e):
                retries -= 1
                time.sleep(1)
            else:
                raise
    raise sqlite3.OperationalError('database is locked after several retries')

class User(UserMixin):
    def __init__(self, id, username, password, role, locked, must_change_password):
        self.id = id
        self.username = username
        self.password = password
        self.role = role
        self.locked = locked
        self.must_change_password = must_change_password

    @staticmethod
    def get(user_id):
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM user WHERE id = ?', (user_id,))
        data = c.fetchone()
        conn.close()
        if data:
            return User(id=data[0], username=data[1], password=data[2], role=data[3], locked=data[4], must_change_password=data[5])
        return None

    @staticmethod
    def find_by_username(username):
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM user WHERE username = ?', (username,))
        data = c.fetchone()
        conn.close()
        if data:
            return User(id=data[0], username=data[1], password=data[2], role=data[3], locked=data[4], must_change_password=data[5])
        return None

    @staticmethod
    def create(username, password, role='user'):
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('INSERT INTO user (username, password, role) VALUES (?, ?, ?)', (username, password, role))
        conn.commit()
        conn.close()

    @staticmethod
    def update_password(user_id, new_password, must_change_password=0):
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('UPDATE user SET password = ?, must_change_password = ? WHERE id = ?', (new_password, must_change_password, user_id))
        conn.commit()
        conn.close()

    @staticmethod
    def lock_user(user_id):
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('UPDATE user SET locked = 1 WHERE id = ?', (user_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def unlock_user(user_id):
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('UPDATE user SET locked = 0 WHERE id = ?', (user_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_user(user_id):
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('DELETE FROM user WHERE id = ?', (user_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_users():
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT id, username, role, locked, must_change_password FROM user')
        users = c.fetchall()
        conn.close()
        return users
