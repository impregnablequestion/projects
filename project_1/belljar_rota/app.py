from flask import Flask, render_template, Blueprint
from controllers.shift_controller import shift_blueprint
from controllers.staff_controller import staff_blueprint

app = Flask(__name__)
app.register_blueprint(shift_blueprint)
app.register_blueprint(staff_blueprint)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)