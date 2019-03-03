from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Gast'}
    return render_template('index.html', title='Home', user=user)