import uuid
from config import Settings
from db import db

from app.auth import auth, get_current_user
from app.category.category_model import Category
from app.inventory.enums.measure import Measure
from app.inventory.inventory_model import Inventory
from utils import MessageCategory, is_image_file
from services import FileService

from flask import Blueprint, flash, redirect, request, render_template
from werkzeug.utils import secure_filename
from sqlalchemy import String, func, or_, select


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

@inventory_bp.route('/estoque/<int:id>', methods=['GET'])
@auth.login_required
def inventory_detail_view(id: int):
    inventory: Inventory | None = db.session.query(Inventory).get(id)

    if inventory is None:
        flash('Item não encontrado.', MessageCategory.ERROR)
        return redirect('/estoque')
    
    categories = db.session.query(Category).all()
    
    context = {
        'user': get_current_user(),
        'inventory': inventory,
        'categories': categories,
        'measures': Measure.get_values()
    }
    return render_template('inventory.detail.html', **context)

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
def inventory_create_action(file_service: FileService = FileService()):
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

    if 'file' not in request.files:
        flash('O campo imagem é obrigatório.', MessageCategory.ERROR)
        return redirect('/estoque/cadastrar')

    file = request.files['file']
    
    if not is_image_file(file.filename):
        flash('O arquivo deve ser uma imagem (PNG, JPG ou JPEG).', MessageCategory.ERROR)
        return redirect('/estoque/cadastrar')

    try:
        image_url = file_service.upload_file(
            bucket=Settings.BUCKET, 
            path=f'/inventory/{uuid.uuid4()}-{secure_filename(file.filename)}', 
            file=file.stream.read()
        )
    except Exception as err:
        flash('Houve um error inesperado ao realizar upload da imagem.', MessageCategory.ERROR)
        return redirect('/estoque/cadastrar')

    try:
        inventory = Inventory(
            data.get('name'), 
            data.get('description'), 
            data.get('category'), 
            data.get('quantity'), 
            data.get('alert_quantity'), 
            data.get('measure'),
            image_url
        )
        db.session.add(inventory)
        db.session.commit()
    except Exception as err:
        flash('Houve um error inesperado ao adicionar item ao estoque.', MessageCategory.ERROR)
        return redirect('/estoque/cadastrar')
    
    flash('Item adicionado ao estoque com sucesso.', MessageCategory.SUCCESS)
    return redirect('/estoque')

@inventory_bp.route('/estoque/<int:id>/atualizar', methods=['POST'])
@auth.login_required
def inventory_update_action(id: int, file_service: FileService = FileService()):
    data = dict(request.form)

    try:
        data = Inventory.validate(data)
    except ValueError as err:
        flash(err.args[0], MessageCategory.ERROR)
        return redirect(f'/estoque/{id}')
    
    inventory: Inventory | None = db.session.query(Inventory).get(id)

    if inventory is None:
        flash('Categoria não encontrada.', MessageCategory.ERROR)
        return redirect('/estoque')

    category = db.session.query(Category).get(data.get('category'))

    if category is None:
        flash('Categoria não encontrada.', MessageCategory.ERROR)
        return redirect(f'/estoque/{id}')

    if 'file' in request.files and request.files['file'].filename != '':
        file = request.files['file']
        
        if not is_image_file(file.filename):
            flash('O arquivo deve ser uma imagem (PNG, JPG ou JPEG).', MessageCategory.ERROR)
            return redirect(f'/estoque/{id}')
        
        try:
            old_path = inventory.get_image_path()
            file_service.remove_file(Settings.BUCKET, old_path)

            image_url = file_service.upload_file(
                bucket=Settings.BUCKET, 
                path=f'/inventory/{uuid.uuid4()}-{secure_filename(file.filename)}', 
                file=file.stream.read()
            )

            data.update({'image_url': image_url})
        except Exception as err:
            flash('Houve um error inesperado ao realizar upload da imagem.', MessageCategory.ERROR)
            return redirect(f'/estoque/{id}')
    else:
        data.update({'image_url': inventory.image_url})

    try:
        inventory.update(data)
        db.session.commit()
    except Exception as err:
        flash('Houve um error inesperado ao adicionar item ao estoque.', MessageCategory.ERROR)
        return redirect(f'/estoque/{id}')
    
    flash('Item atualizado com sucesso.', MessageCategory.SUCCESS)
    return redirect(f'/estoque/{id}')

@inventory_bp.route('/estoque/<int:id>/excluir', methods=['GET'])
@auth.login_required
def inventory_delete_action(id: int, file_service: FileService = FileService()):
    inventory: Inventory | None = db.session.query(Inventory).get(id)

    if inventory is None:
        flash('Item não encontrado.', MessageCategory.ERROR)
        return redirect('/estoque')
    
    try:
        old_path = inventory.get_image_path()
        file_service.remove_file(Settings.BUCKET, old_path)
    except Exception as err:
        print(err)
        flash('Houve um error inesperado ao excluir imagem.', MessageCategory.ERROR)
        return redirect('/estoque')
    
    try:
        db.session.delete(inventory)
        db.session.commit()
    except:
        flash('Houve um error inesperado ao excluir item.', MessageCategory.ERROR)
        return redirect('/estoque')
    
    flash('Item excluido do estoque com sucesso.', MessageCategory.SUCCESS)
    return redirect('/estoque')
