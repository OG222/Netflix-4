from flask import Flask, render_template, request, session
from flask import make_response
from flask import url_for
from flask import redirect


app = Flask(__name__)
app.config['SECRET_KEY'] = "weertyuijkopldssss"

@app.route('/')
def index():
    if session.get("name") == None:
        return redirect(url_for('registration'))
    username = session.get('name', None)
    return render_template('index.html',username=username)
    

@app.route('/registration', methods=['GET','POST'])
def registration():
    session['name'] = None
    if request.method == 'POST':
        form = request.form

        first_name = form['first_name']
        last_name = form['last_name']
        user_name = form['user_name']
        password = form['password']

      
        session['name'] = f'{user_name}'
        return redirect(url_for('index'))
    return render_template('registration.html')


@app.route('/movie/<movie_name>', methods=['GET','POST'])
def movie(movie_name):
    link = request.args.get('link')
    description = 'no description'

    if movie_name == 'bronny_chronicles' :
        description = """this is about a young NBA star who has always wanted to play basket ball but he hails from a 
        very poor background and his parents couldnt just afford to enroll him, one day he had an argument with his 
        father at night the he left for the basket ball court to ease his pain.
        so that faithful night it rained heavy and despite the rain he still played in it,"""

    elif movie_name == 'NATURE' :
        description = """This is movie talks about the beauty of nature and how human activities overtime 
        has degraded the enviroment"""

    elif movie_name == 'THE DEVELOPER TEEN'  :
        description = """This is an animation and it talks about a young guy who has been
          passionate about IT"""

    elif movie_name == 'Clumchin' :
        description == "This is a ficctional movie and it entails"
    
    

        


    username = session.get('name', None)
    return render_template('movie.html', movie_name=movie_name, link=link,username=username, description=description)