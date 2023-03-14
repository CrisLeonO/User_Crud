from flask import render_template, request, redirect
from app import app
from datetime import datetime
from app.models.user import User


@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    return render_template("users.html", users=User.get_all())


# ADD NEW USER
@app.route('/user/new')
def new():
    return render_template("new_user.html")


# SHOW NEW USER AFTER CREATED
@app.route('/user/create', methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')


# SHOW USER
@app.route('/users/show/<int:id>')
def show(id):
    data = {
        "id": id
    }
    return render_template("show.html", user=User.get_one(data))


# DELETE USER
@app.route('/users/remove/<int:user_id>')
def remove_user(user_id):
    data_delete = {
        'id': user_id,
    }
    User.destroy(data_delete)
    return redirect('/users')


#  EDIT USER
@app.route('/user/update/<int:id>')
def edit(id):
    data_one = {
        "id": id
    }
    return render_template("edit_user.html", user=User.get_one(data_one))


#  UPDATE USER
@app.route('/user/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')
