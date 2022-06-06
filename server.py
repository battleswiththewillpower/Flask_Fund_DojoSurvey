from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key="keep it to yourself!"

@app.route('/')
def index():


    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    if 'language' not in request.form:
        session['language'] = 'None selected!'
    else:
        session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    
    # if len(request.form['name']) < 1 and len(request.form['comment']) < 1:
    #   print("name cannot be blank!")
    #   print("comment cannot be blank!")
    #   return redirect('/') 
    # else:

    return redirect('/result')

@app.route('/result')
def result():

    return render_template("result.html")

if __name__=="__main__":
    app.run(debug=True)

  

