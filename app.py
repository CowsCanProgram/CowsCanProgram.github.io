from flask import Flask, render_template, url_for, redirect, request, session, jsonify
import random
import urllib.parse

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

equations = {
    r'E=mc^2': 'Einstein Equation',
    r'a^2+b^2=c^2': 'Pythagorean Equation',
    r'\frac{d}{dx}e^x=e^x': 'd/dx e^x = e^x',
    r'\int_0^{\infty}e^{-x^2}dx=\frac{\sqrt{\pi}}{2}': '∫_0^∞ e^(-x^2) dx = √π/2'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/math')
def math():
    if 'correct_count' not in session:
        session['correct_count'] = 0
    if 'incorrect_count' not in session:
        session['incorrect_count'] = 0

    image_url = request.args.get('image', '')
    equation = request.args.get('equation', '')
    result = request.args.get('result', '')
    correct_answer = request.args.get('correct_answer', '')
    new_image_url = request.args.get('new_image', '')
    new_equation = request.args.get('new_equation', '')

    return render_template('math.html', 
                           image_url=image_url, 
                           equation=equation, 
                           result=result, 
                           correct_answer=correct_answer, 
                           new_image_url=new_image_url, 
                           new_equation=new_equation,
                           correct_count=session['correct_count'],
                           incorrect_count=session['incorrect_count'])



@app.route('/physics')
def physics():
    return render_template('physics.html')

@app.route('/chemistry')
def chemistry():
    return render_template('chemistry.html')

@app.route('/biology')
def biology():
    return render_template('biology.html')


@app.route('/hodgepodge')
def hodgepodge():
    return render_template('hodgepodge.html')

@app.route('/random_math')
def random_math():
    equation = random.choice(list(equations.keys()))
    encoded_equation = urllib.parse.quote_plus(equation)
    image_url = f'https://latex.codecogs.com/svg.latex?{encoded_equation}'
    return redirect(url_for('math', image=image_url, equation=equation))

@app.route('/check_answer', methods=['POST'])
def check_answer():
    user_answer = request.form.get('user_answer')
    equation = request.form.get('equation')
    correct_answer = equations.get(equation, '')

    if user_answer == correct_answer:
        result = 'Correct'
        session['correct_count'] = session.get('correct_count', 0) + 1
    else:
        result = 'Incorrect'
        session['incorrect_count'] = session.get('incorrect_count', 0) + 1

    # Generate a new random equation for the next question
    new_equation = random.choice(list(equations.keys()))
    encoded_new_equation = urllib.parse.quote_plus(new_equation)
    new_image_url = f'https://latex.codecogs.com/svg.latex?{encoded_new_equation}'

    return redirect(url_for('math', 
                            image=new_image_url, 
                            equation=new_equation, 
                            result=result, 
                            correct_answer=correct_answer, 
                            new_image=new_image_url, 
                            new_equation=new_equation))

    
@app.route('/reset_session')
def reset_session():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)