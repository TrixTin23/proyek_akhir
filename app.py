from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        flash('Login requested for user {}, remember_me={}'.format(
            request.form['username'], request.form['remember_me']))
        return redirect(url_for('index'))
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000)
