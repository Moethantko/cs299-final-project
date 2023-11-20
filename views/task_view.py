from flask import Blueprint, request, redirect
from flask import render_template, g, Blueprint
from models.task import Task, TaskDB

task_list_blueprint = Blueprint('task_list_blueprint', __name__)


@task_list_blueprint.route('/', methods=["GET"])
def index():
    database = TaskDB(g.mysql_db, g.mysql_cursor)
    todo_list = database.select_all_tasks()
    return render_template('index.html', todo_list=todo_list)

@task_list_blueprint.route('/task-entry', methods=["GET"])
def task_entry():
   return render_template("task_entry.html")

@task_list_blueprint.route('/add-task', methods=["POST"])
def add_task():
   task_description = request.form.get("task_description")

   new_task = Task(task_description)
   database = TaskDB(g.mysql_db, g.mysql_cursor)

   database.insert_task(new_task)

   return redirect('/')

@task_list_blueprint.route('/', methods=["POST"])
def delete_tasks():
   database = TaskDB(g.mysql_db, g.mysql_cursor)

   task_ids = request.form.getlist("task_item")
   for id in task_ids:
       database.delete_task_by_id(id)

   return render_template('index.html', todo_list=database.select_all_tasks())
