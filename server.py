from flask import Flask, render_template , request , redirect, session  # Render_template(s) is a Method (or a function), Request is a property or a Attribute, Redirect is a Method (or a function), Session is a Attribute or a Property.

from env import key


app = Flask(__name__)


app.secret_key = key  # Meaningful random characters and numbers that help keep my Users information secure. Can also store them on another module to keep it more secure or to "bury it".


@app.route('/')
def home():
    print('Hello World!')
    print(request.form)  # Every Request.form will have a key and a STRING VALUE!! No matter what "Type" of Input I have, when it comes in to request.form and I have it on my Server it is a STRING, It won't be number it wont be a boolean it is a STRING. So If I ever need to do something with the Data that came in (i.e age, or birthday) I need to make sure im doing the right things in my modules. (Maybe will nee to convert somethings, or use jinja in my html...)
    print(session)  # Sessions are ImmutableMultiDict Like The Request.form. But they hold on to Users "Session" during their time on my website. Sessions are stored as key:value pairs and I treat them like I would a normal dictionary (like I would the Request.form ImmutableMultiDict). Except the information inside of them are stored as a tuple (I would then have to figure out how to "change" them).
    if 'key' in session:  # If check, checking to seeing if a certain key for my Session is present in my Session ImmutableMultiDict. And if so then do what is in my code block.
        print('yay')
        session['key'] += 1
    else:
        print('no')
        session['key'] = 1
    return render_template('index.html')


@app.route('/submit_info', methods=['POST'])
def submit_info():
    print('Hello you are here!')
    print(request.form)  # Print Statements to control the flow of my code and to debug!!
    session['fname'] = request.form['f_name']  # I can create a session key for the Session ImmutableMultiDict and set it to some data from my request.form, to save the SESSION for that User.
    session['lname'] = request.form['l_name']
    session['pword'] = request.form['p_word']
    print(session)
    return redirect('/')  # ALWAYS Redirect on POST methods.


@app.route('/clear')
def destroy_session():
    session.clear()
    return redirect('/')


@app.route('/add_two')
def add_two():
    if 'key' in session:
        session['key'] += 1
    else:
        session['key'] = 0
    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()
    if 'key' != session:
        session['key'] = 0
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)