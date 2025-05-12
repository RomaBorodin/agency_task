from flask import render_template, request, redirect, url_for
from .models import Agent
from . import db
from . import app


@app.route("/")
def home():
    agents_list = Agent.query.all()
    return render_template("index.html", agents_list=agents_list)
