from flask import Flask, jsonify

from demo_database import get_followers
from CONSTANTS.GENERAL import JSON


app = Flask(__name__)


@app.route('/')
def welcome_message() -> JSON:
    '''
    Function to welcome reader.
    '''
    return jsonify('Hello Lun!')


@app.route('/users/<user_id>/followers', methods= ['GET'])
def get_followers_of_id(user_id: int) -> JSON:
    '''
    Function to get the followers of <user_id>.
    '''
    followers = get_followers(user_id)
    return jsonify({'response': followers})