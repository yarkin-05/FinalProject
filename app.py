
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False


@app.route('/')
def index():
    
    return render_template('registro.html',)

if __name__ == '__main__':
    app.run()
