from flask import Blueprint, flash, redirect, url_for, render_template, request, session
from app import db
from app.models.task import Task

task_bp = Blueprint('task_bp', __name__)

@task_bp.route('/')
def view_task():
    if 'user_id' not in session:
        flash('Login required to view tasks.', 'danger')
        return redirect(url_for('auth_bp.login'))
    
    tasks = Task.query.filter_by(user_id=session['user_id']).all()
    return render_template('tasks.html', tasks=tasks)

@task_bp.route('/add', methods=['POST'])
def add_task():
    if 'user_id' not in session:
        return redirect(url_for('auth_bp.login'))
    
    title = request.form.get('title')
    if title:
        new_task = Task(title=title, status='Pending', user_id=session['user_id'])  # 👈 assign user
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully!', 'success')
    return redirect(url_for('task_bp.view_task'))


@task_bp.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_status(task_id):
    if 'user_id' not in session:
        flash('Login required to toggle task status.', 'danger')
        return redirect(url_for('auth_bp.login'))

    task = Task.query.get(task_id)
    if task:
        if task.status == 'Pending':
            task.status = 'Working'
        elif task.status == 'Working':
            task.status = 'Done'
        else:
            task.status = 'Pending'
        db.session.commit()
    return redirect(url_for('task_bp.view_task'))

@task_bp.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 'user_id' not in session:
        flash('Please login to delete a task.', 'danger')
        return redirect(url_for('auth_bp.login'))

    task_to_delete = Task.query.get_or_404(task_id)
    if task_to_delete.user_id != session['user_id']:
        flash('Unauthorized action.', 'danger')
        return redirect(url_for('task_bp.view_task'))
    
    # delete logic
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for('task_bp.view_task'))

@task_bp.route('/clear', methods=['POST'])
def clear_tasks():
    if 'user_id' not in session:
        flash('Please login to clear tasks.', 'danger')
        return redirect(url_for('auth_bp.login'))

    Task.query.delete()
    db.session.commit()
    flash('All tasks cleared!', 'info')
    return redirect(url_for('task_bp.view_task'))
