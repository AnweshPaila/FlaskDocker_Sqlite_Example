from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Names(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        submittedName = request.form['name']
        newName = Names(Name=submittedName)

        try:
            db.session.add(newName)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return str(e)

    else:
        names = Names.query.order_by(Names.id).all()
        return render_template('index.html', dbNames=names)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
