from shared import app
import methods
from flask import Flask, render_template, request, redirect, url_for, abort
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns


@app.route('/')
def index():
    todos = methods.get_all_todos().to_dict('records')
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name')
    if not name:
        abort(400, "Name property missing!")
    methods.add_todo(name)
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete(todo_id):
    methods.delete_todo(todo_id)
    return redirect(url_for('index'))

@app.route('/edit/<int:todo_id>', methods=['POST'])
def edit(todo_id):
    name = request.form.get('name')
    completed = request.form.get('completed') == 'on'
    if name:
        methods.update_todo(todo_id, name=name, completed=completed)
    else:
        methods.update_todo(todo_id, completed=completed)
    return redirect(url_for('index'))