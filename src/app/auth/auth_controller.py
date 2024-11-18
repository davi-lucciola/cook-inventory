from db import db
import flask_login as auth
from app.user.user_model import User
from utils import MessageCategory
from flask import Blueprint, flash, redirect, request, render_template


auth_bp = Blueprint('Auth', __name__, template_folder='./views')


@auth_bp.route('/login', methods=['GET'])
def login_view():
    return render_template('login.html')

@auth_bp.route('/login', methods=['POST'])
def login_action():
    data = request.form

    if data.get('username') is None or data.get('username').strip() == '':
        flash('O campo usuário é obrigatório.', MessageCategory.ERROR)
        return redirect('/login')
    
    if data.get('password') is None or data.get('password').strip() == '':
        flash('O campo senha é obrigatório.', MessageCategory.ERROR)
        return redirect('/login')
    
    user = db.session.query(User)\
        .where(User.name == data.get('username')).first()

    if user is None or user.verify_password(data.get('password')) is False:
        flash('Credenciais Inválidas.', MessageCategory.ERROR)
        return redirect('/login')
    
    auth.login_user(user, remember=data.get('remember'))
    return redirect('/comidas')