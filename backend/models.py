from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Policy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    raw_text = db.Column(db.Text)
    summary = db.Column(db.Text)
    stakeholders = db.Column(db.JSON)
    impact_score = db.Column(db.Float)
