from elections.db import db
import datetime

class Vote(db.Model):
    __tablename__ = 'vote'
    election = db.Column(db.ForeignKey('election.id'))
    candidate = db.Column(db.ForeignKey('candidate.id'))
    date_placed = db.Column(db.DateTime, default=datetime.datetime.utcnow)
