from flask import Flask, render_template, url_for, redirect, request
import random
import urllib.parse

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/math')
def math():
    image_url = request.args.get('image', '')
    if not image_url:
        image_url = None
    return render_template('math.html', image_url=image_url)


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
    # Generate a random LaTeX equation
    equations = [
        r'$E=mc^2$',
        r'$a^2 + b^2 = c^2$',
        r'$ \frac{d}{dx} e^x = e^x $',
        r'$ \int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2} $'
    ]
    equation = random.choice(equations)

    encoded_equation = urllib.parse.quote(equation)
    image_url = f'https://latex.codecogs.com/png.latex?{encoded_equation}'

    return redirect(url_for('math', image=image_url))

if __name__ == '__main__':
    app.run(debug=True)