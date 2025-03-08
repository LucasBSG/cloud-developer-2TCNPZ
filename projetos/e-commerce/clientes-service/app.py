from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

@app.route('/')
def home():
    form = RegistrationForm()
    return render_template('home.html', form=form)

@app.route('/status')
def status():
    return jsonify({"status": "ok"})

@app.route('/users')
def users():
    return jsonify({
        "nome": "Jesualdo",
        "data_implantacao": "06-03-2025"
    })

@app.route('/register', methods=['POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        # Aqui você pode adicionar a lógica para salvar o usuário e a senha no banco de dados
        return redirect(url_for('home'))
    return render_template('home.html', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)