import os
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from models import db

from models import MyUser

app = Flask(__name__)

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        print(request.method)
        userid = request.form.get('userid')
        username = request.form.get('username')
        password = request.form.get('password')
        re_password = request.form.get('re‐password')

        if (userid and username and password and re_password) and (password == re_password):
             myuser = MyUser()
             myuser.userid = userid
             myuser.username = username
             myuser.password = password

             db.session.add(myuser)
             db.session.commit()
        return redirect('/')

    return render_template('register.html')


@app.route('/', methods=['GET','POST'])
def hello():
    return render_template('hello.html')




if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__))
    dbfile = os.path.join(basedir, "db.sqlite")

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    db.app = app
    db.create_all()
    app.run(host='127.0.0.1', port = 5000, debug = True)