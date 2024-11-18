import flask_login as auth
from flask import Blueprint, flash, redirect, request, render_template


food_bp = Blueprint('Food', __name__, template_folder='./views')


@food_bp.route('/comidas', methods=['GET'])
@auth.login_required
def index():
    return render_template('list.html')