from flask import Flask, jsonify, request
from db import Item, session
from utils import row_to_dict
from datetime import datetime


app = Flask(__name__)


 
@app.route('/item/list')
def list_all_items():
    pass
    

@app.route('/item/<int:item_id>')
def get_item_by_id(item_id):
    pass


@app.route('/item/new', methods = ['POST'])
def create_new_item():
    pass


@app.route('/item/filter')
def filter_items():
    pass


@app.route('/item/<int:item_id>/comment/update', methods = ['PUT'])
def update_item(item_id):
    pass


@app.teardown_appcontext
# Housekeeping
def cleanup(arg):
    session.remove()