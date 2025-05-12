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


@app.route("/agent/<int:id>")
def get_agent(id):
    agent = Agent.query.get(id)
    return render_template("get_agent.html", agent=agent)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_agent(id):
    agent = Agent.query.get_or_404(id)
    if request.method == "POST":
        raw_info = {
            "name": request.form["name"],
            "number": request.form["number"],
            "email": request.form["email"],
            "level": request.form["level"]
        }

        new_info = {key: value for key, value in raw_info.items() if value and value.strip()}
        for k, v in new_info.items():
            setattr(agent, k, v)

        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit_agent.html", agent=agent)
