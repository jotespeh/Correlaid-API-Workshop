from flask import Flask, jsonify, request
from db import Item, session
from utils import row_to_dict
from datetime import datetime

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
    comment = f"%{request.json.get('comment')}%"
    title = f"%{request.json.get('title')}%"
    query = session.query(Item).filter(Item.comment.like(comment), Item.title.like(title)).all()
    result = [row_to_dict(row) for row in query]
    return(jsonify(result))


@app.route('/item/new', methods = ['POST'])
def create_new_item():
    item = request.json 
    # TODO: Check for failure, try/except block
    new_item = Item()
    new_item.comment = item.get('comment')
    new_item.title = item.get('title')
    new_item.date_added = datetime.now()
    session.add(new_item)
    session.commit()
    result = {"id": new_item.id, "title": new_item.title,
              "comment": new_item.comment, "date_added": new_item.date_added}
    return((jsonify(result), 201))


@app.route('/item/<int:item_id>/comment/update', methods = ['PUT'])
def update_item(item_id):
    comment = request.json.get("comment")
    if not comment:
        return(jsonify({}), 400)
    new_item = session.query(Item).filter(Item.id == item_id).update({'comment': comment})
    result = row_to_dict(session.query(Item).filter(Item.id == item_id).first())
    session.commit()
    return((jsonify(result), 201))


@app.teardown_appcontext
# Housekeeping
def cleanup(arg):
    session.remove()