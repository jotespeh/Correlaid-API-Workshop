from flask import Flask, jsonify, request
from db import Item, session
from utils import row_to_dict

app = Flask(__name__)

 
@app.route('/item/list')
def list_all_items():
    result = []
    
    query = session.query(Item).all()
    result = [row_to_dict(row) for row in query]
    
    return(jsonify(result))
    
@app.route('/item/<int:item_id>')
def get_item_by_id(item_id):
    query = session.query(Item).filter(Item.id == item_id).first()
    return(row_to_dict(query))

@app.route('/item/filter')
def filter_items():
    # TODO: Try except, allow for more arguments
    comment = f"%{request.args.get('comment')}%"
    query = session.query(Item).filter(Item.comment.like(comment)).all()
    result = [row_to_dict(row) for row in query]

    return(jsonify(result))


@app.route('/item/new')
def create_new_item(methods = ['POST']):
    item = request.json 
    # TODO: Check for failure, try/except block
    new_item = Item()
    new_item.comment = item.get('comment')
    new_item.title = item.get('title')
    session.add(new_item)
    session.commit()
    return((jsonify(item), 201))

@app.route('/item/<int:item_id>/update')
def update_item(item_id, methods = ['PUT']):
    pass


@app.teardown_appcontext
# Housekeeping
def cleanup(arg):
    session.remove()