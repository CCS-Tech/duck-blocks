from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), index=True,  unique=True)
    password = db.Column(db.String(250), index=True, unique=False)
    email = db.Column(db.String(120), index=True, unique=True)

class HTML_Sections(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)

class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(250), unique=True)
    tag_type = db.Column(db.String(250))
    section_id = db.Column(db.Integer, db.ForeignKey('HTML_Sections.id'))

class Tag_Attrs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    attr_1_name = db.Column(db.String(120))
    attr_1_value = db.Column(db.String(250))
    attr_2_name = db.Column(db.String(120))
    attr_2_value = db.Column(db.String(250))
    attr_3_name = db.Column(db.String(120))
    attr_3_value = db.Column(db.String(250))
    attr_4_name = db.Column(db.String(120))
    attr_4_value = db.Column(db.String(250))
    attr_5_name = db.Column(db.String(120))
    attr_5_value = db.Column(db.String(250))
    tag_id = db.Column(db.Integer, db.ForeignKey('Tags.id'))
