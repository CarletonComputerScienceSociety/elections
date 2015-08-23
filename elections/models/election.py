from elections.db import db


# Table mapping between elections and candidates
candidate_association = db.Table(
        'election_candidates', db.Model.metadata,
        db.Column('election_id', db.Integer, db.ForeignKey('election.id')),
        db.Column('candidate_key', db.Integer, db.ForeignKey('candidate.id')),
    )


class Election(db.Model):
    __tablename__ = 'election'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    explanation = db.Column(db.Text)

    candidates = db.relationship('Candidate', secondary=candidate_association)
