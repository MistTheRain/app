from flask import Flask, render_template, request, redirect, url_for, abort, session
import main


app = Flask(__name__)
app.config['SECRET_KEY'] = 'F34TF$($e34D';

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    session['location'] = request.form['location']
    session['dist'] = request.form['dist']
    return redirect(url_for('calculate'))

@app.route('/calculate')
def calculate():
    #a = session['location']
    output_data = main.get_location_data(session['location'], session['dist'])
    session['place'] = output_data[0]
    #return output_data[0]
    return redirect(url_for('results', loc=session['location'], plac=session['place']))
	
@app.route('/results')
def results():
    loc = request.args.get('loc')
    plac = request.args.get('plac')
    return render_template('results.html', loc=loc, plac=plac)


if __name__ == '__main__':
    app.run()