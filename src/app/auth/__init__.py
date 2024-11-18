from db import db
from flask import flash, redirect
from flask_login import LoginManager
from app.user.user_model import User
from utils import MessageCategory


# Instância do LoginManager.
auth = LoginManager()


# Função que carrega o usuário logado no contexto de autenticação quando uma requisição é realizada.
@auth.user_loader
def load_user(id: int) -> User:
    return db.session.query(User).get(id)

# Função que lida quando uma requisição é feita em uma rota protegida quando o cliente não está autenticada.
@auth.unauthorized_handler
def unauthorized_handler():
    flash('Não autenticado. Por favor entre com sua conta.', category=MessageCategory.ERROR)
    return redirect('/login')