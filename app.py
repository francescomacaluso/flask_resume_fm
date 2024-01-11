from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

# Create an Index Page
@app.route('/')
def index():

    start_date = datetime(year=2014, month=1, day=1)
    today = datetime.today()
    years_of_experience = today.year - start_date.year
    full_name = 'Francesco Macaluso'

    return render_template('index.html',f_name=full_name,years_of_experience=years_of_experience)

# Create the About Page
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
