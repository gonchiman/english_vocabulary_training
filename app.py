from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        page_title='English Vocabulary Training'
    )

@app.route('/registration')
def registration():
    return render_template(
        'registration.html',
        page_title='Register Word'
    )

if __name__ == '__main__':
    app.run(debug=True)