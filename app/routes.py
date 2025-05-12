from flask import render_template, request, redirect, url_for
from .models import Agent
from . import db
from . import app


@app.route("/")
def home():
    agents_list = Agent.query.all()
    return render_template("index.html", agents_list=agents_list)

@app.route("/add", methods=["GET", "POST"])
def add_agent():
    if request.method == "POST":
        agent_data = {
            "name": request.form["name"],
            "number": request.form["number"],
            "email": request.form["email"],
            "level": request.form["level"]
        }

        for k, v in agent_data.items():
            if not v.strip():
                return redirect(url_for('home'))

        new_agent = Agent(**agent_data)
        db.session.add(new_agent)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("add_agent.html")
