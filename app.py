from flask import Flask, request, render_template, jsonify, session
from boggle import Boggle

app = Flask(__name__)


boggle_game = Boggle()

@app.route("/")
def homepage():
    """Top page"""

    board = boggle_game.make_board()
    session['board'] = board
    