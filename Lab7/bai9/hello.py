from flask import render_template, Flask
app = Flask(__name__, static_folder='D:\\Python\\PythonTH\\Lab7\\bai9\\templates\\static' )

@app.route('/')
def index():
    return render_template("abc.html")

if __name__ == '__main__':
    app.run(port=5050)