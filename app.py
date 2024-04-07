from flask import Flask, render_template, request, flash, redirect, url_for
from example_blueprint import example_blueprint

app = Flask(__name__)
app.register_blueprint(example_blueprint)
app.config['SECRET_KEY'] = 'fjdsbfjksfjdsbfbvjhbdhjbvkjrebjkrvk'

  # Code to make replit servers work
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)

