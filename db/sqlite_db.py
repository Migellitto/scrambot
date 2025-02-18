"""
CREATE TABLE tasks (
	task_id INTEGER PRIMARY KEY AUTOINCREMENT,
	task_name TEXT,
	task_month INTEGER,
	task_is_active BOOLEAN
);
"""
import sqlalchemy as db
from rest import get_month

def sqlite_db_engine():
    engine = db.create_engine('sqlite:///db/tasks.db')
    return engine

def sqlite_conn():
    conn = sqlite_db_engine().connect()
    return conn

metadata = db.MetaData()

tasks = db.Table('tasks', metadata, db.Column('task_id', db.Integer, primary_key=True, autoincrement=True), \
                 db.Column('task_name', db.Text), \
                 db.Column('task_month', db.Integer), \
                 db.Column('task_is_active', db.Boolean, default=False))

# metadata.create_all(sqlite_db_engine())

def sqlite_select_all_task():
    select = db.select(tasks)
    conn = sqlite_conn()
    select_all_results = conn.execute(select)
    return select_all_results.fetchall()

def sqlite_select_all(month):
    slt = db.select(tasks).where(tasks.columns.task_month == int(month))
    conn = sqlite_conn()
    select_all_results = conn.execute(slt)
    return select_all_results.fetchall()

def sqlite_task_id_update_0(task_id):
    upd = db.update(tasks).where(tasks.columns.task_id == task_id).values(task_is_active=0)
    conn = sqlite_conn()
    conn.execute(upd)
    conn.commit()

def sqlite_task_id_update_1(task_id):
    upd = db.update(tasks).where(tasks.columns.task_id == task_id).values(task_is_active=1)
    conn = sqlite_conn()
    conn.execute(upd)
    conn.commit()

def sqlite_insert_new_task(task_name):
    insrt = db.insert(tasks).values(task_name=task_name, task_month=get_month()[0], task_is_active=1)
    conn = sqlite_conn()
    conn.execute(insrt)
    conn.commit()


# print(sqlite_select_all(2))