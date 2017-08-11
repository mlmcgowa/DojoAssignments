from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)


@app.route('/')
def survey():
    return render_template('index.html')


@app.route('/result', methods=['post'])
def create_user():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    Boolean = False

    if len(request.form['name']) < 1:
        flash('This Name Field cannot be empty!')
        Boolean = True
        # return redirect('/')
    if len(request.form['comment']) < 1:
        flash('This Comment Field cannot be empty!')
        Boolean = True
        # return redirect('/')
    if len(request.form['comment']) > 150:
        flash('comment can only be 150 characters')
        Boolean = True
        # return redirect('/')

    if Boolean = True:
        return redirect('/')
    else:
        return render_template('/result.html', name = name, location = location, language = language, comment = comment)




app.run(debug=True)
