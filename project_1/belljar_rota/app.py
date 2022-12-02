from flask import Flask, render_template

# from controllers import blueprints

app = Flask(__name__)

# app.register_blueprint(staff_blueprint)
# app.register_blueprint(shifts_blueprint)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)