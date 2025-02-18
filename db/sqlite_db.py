"""
CREATE TABLE tasks (
	task_id INTEGER PRIMARY KEY AUTOINCREMENT,
	task_name TEXT,
	task_month INTEGER,
	task_is_active BOOLEAN
);
"""
import sqlalchemy as db
from sqlalchemy import func
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

def sqlite_delete_task(task_id):
    dlt = db.delete(tasks).where(tasks.columns.task_id == task_id)
    conn = sqlite_conn()
    conn.execute(dlt)
    conn.commit()

def sqlite_if_not_add_tasks_month():
    max_id = func.max(tasks.columns.task_id)
    conn = sqlite_conn()
    max_id = conn.execute(max_id).one()[0]
    # print(f"MAX ID: {max_id}")
    slt = db.select(tasks.columns.task_month).where(tasks.columns.task_id == int(max_id))
    conn = sqlite_conn()
    month = int(conn.execute(slt).one()[0])
    slt = db.select(tasks).where(tasks.columns.task_month == month)
    conn = sqlite_conn()
    select_all_results = conn.execute(slt).fetchall()
    # print(f"за месяц {month} записи в БД: {select_all_results}")
    month = int(get_month()[0])
    for row in select_all_results:
        # print(f"Добавляем в БД строку {row[1]}, {month}, 1")
        insrt = db.insert(tasks).values(task_name=row[1], task_month=month, task_is_active=1)
        conn = sqlite_conn()
        conn.execute(insrt)
        conn.commit()