from app.inventory.enums.measure import Measure
from db import db
from app.auth import auth, get_current_user
from app.category.category_model import Category
from app.inventory.inventory_model import Inventory

from flask import Blueprint, flash, redirect, request, render_template
from sqlalchemy import String, func, or_, select
from utils import MessageCategory


inventory_bp = Blueprint('Inventory', __name__, template_folder='./views')


@inventory_bp.route('/estoque', methods=['GET'])
@auth.login_required
def inventory_index_view():
    params = dict(request.args)
    query = select(Inventory).join(Category, Inventory.category)

    if params.get('search') is not None:
        query = query.where(
            or_(
                Inventory.name.ilike(f'%{params.get("search")}%'),
                Category.name.ilike(f'%{params.get("search")}%'),
                func.cast(Inventory.quantity, String()).ilike(f'%{params.get("search")}%'),
                func.cast(Inventory.alert_quantity, String()).ilike(f'%{params.get("search")}%')
            )
        )

    inventories = db.session.execute(query).scalars().all()

    context = {
        'user': get_current_user(),
        'inventories': inventories,
        'measures': Measure.get_values()
    }
    return render_template('inventory.index.html', **context)

@inventory_bp.route('/estoque/cadastrar', methods=['GET'])
@auth.login_required
def inventory_create_view():
    categories = db.session.query(Category).all()

    if len(categories) == 0:
        # Por algum motivo, nessa linha de codigo 
        # se o ".value" não for especificado ele não funciona.
        flash('Você não tem categorias cadastradas.', MessageCategory.WARNING.value)

    context = {
        'user': get_current_user(),
        'categories': categories,
        'measures': Measure.get_values().items()
    }

    return render_template('inventory.create.html', **context)

@inventory_bp.route('/estoque/cadastrar', methods=['POST'])
@auth.login_required
def inventory_create_action():
    data = dict(request.form)

    try:
        data = Inventory.validate(data)
    except ValueError as err:
        flash(err.args[0], MessageCategory.ERROR)
        return redirect('/estoque/cadastrar')
    
    category = db.session.query(Category).get(data.get('category'))

    if category is None:
        flash('Categoria não encontrada.', MessageCategory.ERROR)
        return redirect('/estoque/cadastrar')
    
    try:
        inventory = Inventory(
            data.get('name'), 
            data.get('description'), 
            data.get('category'), 
            data.get('quantity'), 
            data.get('alert_quantity'), 
            data.get('measure')
        )
        db.session.add(inventory)
        db.session.commit()
    except Exception as err:
        print(err)
        flash('Houve um error inesperado ao adicionar item ao estoque.', MessageCategory.ERROR)
        return redirect('/estoque/cadastrar')
    
    flash('Item adicionado ao estoque com sucesso.', MessageCategory.SUCCESS)
    return redirect('/estoque')
