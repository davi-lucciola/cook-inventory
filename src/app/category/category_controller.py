from db import db
from app.auth import auth, get_current_user
from app.category.category_model import Category
from utils import MessageCategory
from flask import Blueprint, flash, redirect, render_template, request
from sqlalchemy import select


category_bp = Blueprint('Category', __name__, template_folder='./views')


@category_bp.route('/categorias', methods=['GET'])
@auth.login_required
def category_index_view():
    params = dict(request.args)
    query = select(Category)

    if params.get('search') is not None:
        query = query.where(Category.name.ilike(f'%{params.get("search")}%'))

    categories = db.session.execute(query).scalars().all()
    
    context = {
        'user': get_current_user(),
        'categories': categories
    }
    
    return render_template('category.index.html', **context)


@category_bp.route('/categorias/cadastrar', methods=['GET'])
@auth.login_required
def category_create_view():
    return render_template('category.create.html', user=get_current_user())


@category_bp.route('/categorias/cadastrar', methods=['POST'])
@auth.login_required
def category_create_action():
    data = dict(request.form)

    if data.get('name') is None or data.get('name').strip() == '':
        flash('O campo nome é obrigatório.', MessageCategory.ERROR)
        return redirect('/categorias/cadastrar')

    if data.get('description').strip() == '':
        data.update({'description': None})

    try:
        category = Category(data.get('name'), data.get('description'))
        db.session.add(category)
        db.session.commit()
    except:
        flash('Houve um error inesperado ao cadastrar categoria.', MessageCategory.ERROR)
        return redirect('/categorias/cadastrar')

    flash('Categoria cadastrada com sucesso.', MessageCategory.SUCCESS)
    return redirect('/categorias')


@category_bp.route('/categorias/<int:id>/atualizar', methods=['GET'])
@auth.login_required
def category_update_view(id: int):
    category = db.session.query(Category).get(id)

    if category is None:
        flash('Categoria não encontrada.', MessageCategory.ERROR)
        return redirect('/categorias')
    
    context = {
        'user': get_current_user(),
        'category': category
    }

    return render_template('category.update.html', **context)


@category_bp.route('/categorias/<int:id>/atualizar', methods=['POST'])
@auth.login_required
def category_update_action(id: int):
    data = dict(request.form)
    category: Category = db.session.query(Category).get(id)

    if category is None:
        flash('Categoria não encontrada.', MessageCategory.ERROR)
        return redirect('/categorias')

    if data.get('name') is None or data.get('name').strip() == '':
        flash('O campo nome é obrigatório.', MessageCategory.ERROR)
        return redirect(f'/categorias/{id}/atualizar')

    if data.get('description').strip() == '':
        data.update({'description': None})

    try:
        category.update(data)
        db.session.commit()
    except:
        flash('Houve um error inesperado ao atualizar categoria.', MessageCategory.ERROR)
        return redirect(f'/categorias/{id}/atualizar')
    

    flash('Categoria atualizada com sucesso.', MessageCategory.SUCCESS)
    return redirect('/categorias')


@category_bp.route('/categorias/<int:id>/excluir', methods=['GET'])
@auth.login_required
def category_delete_action(id: int):
    category = db.session.query(Category).get(id)

    if category is None:
        flash('Categoria não encontrada.', MessageCategory.ERROR)
        return redirect('/categorias')
    
    try:
        db.session.delete(category)
        db.session.commit()
    except:
        flash('Houve um error inesperado ao excluir categoria.', MessageCategory.ERROR)
        return redirect('/categorias')

    flash('Categoria excluída com sucesso.', MessageCategory.SUCCESS)
    return redirect('/categorias')
