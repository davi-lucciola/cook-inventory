from db import db
import flask_login as auth
from flask import flash, redirect
from app.user.user_model import User
from utils import MessageCategory


# Instância do LoginManager.
login_manager = auth.LoginManager()


# Função que carrega o usuário logado no contexto de autenticação quando uma requisição é realizada.
@login_manager.user_loader
def load_user(id: int) -> User:
    return db.session.query(User).get(id)

# Função que lida quando uma requisição é feita em uma rota protegida quando o cliente não está autenticada.
@login_manager.unauthorized_handler
def unauthorized_handler():
    flash('Não autenticado. Por favor entre com sua conta.', category=MessageCategory.ERROR)
    return redirect('/login')

def get_current_user() -> auth.UserMixin:
    return auth.current_user