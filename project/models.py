from datetime import datetime

from project import db


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    middle_name = db.Column(db.String(120), nullable=False)
    position = db.Column(db.String(120), nullable=False)
    chair = db.Column(db.String(120), nullable=False)
    date_start = db.Column(db.Date(), nullable=False)
    phone = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Teacher {self.first_name} {self.last_name} >'

    @classmethod
    def create(cls, first_name, last_name, middle_name, position, chair, date_start, phone):
        teacher = cls(
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            position=position,
            chair=chair,
            date_start=datetime.strptime(date_start, "%d/%m/%Y").date(),
            phone=phone
        )
        db.session.add(teacher)
        db.session.commit()

    @classmethod
    def get(cls, teacher_id):
        obj = vars(db.session.query(cls).first())
        obj.pop('_sa_instance_state')
        return obj
