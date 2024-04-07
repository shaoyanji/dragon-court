from flask import Flask, render_template, request, flash, redirect, url_for
from example_blueprint import example_blueprint
app = Flask(__name__)
app.register_blueprint(example_blueprint)

  # Code to make replit servers work
if __name__ == '__main__':
    port = 8081
    port = int(port)

    app.run(port=port,host='0.0.0.0')
