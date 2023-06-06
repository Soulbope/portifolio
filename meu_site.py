from flask import Flask, render_template, url_for

app = Flask(__name__)

#site aqui

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/blog-single.html')
def blogsingle():
    return render_template("blog-single.html")

with app.test_request_context():
    print(url_for('static', filename='style.css'))

# #deploy do site
if __name__ == "__main__":
    app.run()