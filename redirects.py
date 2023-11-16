from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for an about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for a contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
