from . import db


class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    number = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Agent {self.name}>"
