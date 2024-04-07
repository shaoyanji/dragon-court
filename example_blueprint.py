from flask import Blueprint, render_template, request, flash, redirect, url_for
#from ola import *

from gem_custom import *
example_blueprint = Blueprint('example_blueprint', __name__)


messages = [{
    'id': 'Message One',
    'content': 'Message One Content',
    'aicontent': 'AI Generated Content'
}, {
    'id': 'Message Two',
    'content': 'Message Two Content',
    'aicontent': 'Message Three Content'
}]

@example_blueprint.route('/')
def index():
  return render_template('index.html', messages=messages)


@example_blueprint.route('/profile')
def profile():
    return "This is the profile page"

@example_blueprint.route('/submit_message', methods=['POST'])
def submit_message():
  # Process form data
  content = request.form['content']
  id= "FLOW"
  if not content:
    flash('Content is required!')
  else:
    # Add message to the list
    aicontent = ai('', content)
    #aicontent = "i liked this"

    
    messages.append({
        'id': id,
        'content': content,
        'aicontent': aicontent
    })

  # Render the updated message container HTML
#  return render_template('message_cards.html', messages=messages)
  return render_template('message_card.html', message=messages[-1])