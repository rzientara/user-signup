from flask import Flask, request, redirect, render_template
import re
app = Flask('app')

@app.route('/')
def index():
  return render_template('index.html', user_error='', pass_error='', verify_error='', email_error='')

@app.route('/validate', methods=['POST'])
def validate():
  username = request.form['username']
  password = request.form['password']
  verify = request.form['verify']
  email = request.form['email']

  messages = ["That's not a valid username",
              "That's not a valid password",
              "Passwords don't match",
              "That's not a valid email"]

  #reset error status
  error = False

  #list containing the valid status of user inputs.
  try:
    val_list
  except:
    val_list = ['', '', '', '']

  #validate username has proper length and no spaces.
  val_list[0] = re.search('^.{3,21}$', username)
  if re.search(' ', username):
    val_list[0] = None

  #validate password has proper length and no spaces.
  val_list[1] = re.search('^.{3,21}$', password)
  if re.search(' ', password):
    val_list[1] = None

  #validate password and repeated password match.
  if password != verify:
    val_list[2] = None
  else:
    val_list[2] = ""

  #validate email length and format.
  val_list[3] = re.search('^.{3,21}$', email)
  if email != '':
    if re.search(' ', email) or re.search('[@]', email) == None or re.search('[.]', email) == None:
      val_list[3] = None
  else:
    val_list[3] = ""

  #if a user input is invalid, replace its value with the appropriate error message and set Error to True.
  #if the input is valid, replace its value with empty string.
  for item in val_list:
    if item == None:
      val_list[val_list.index(item)] = messages[val_list.index(item)]
      error = True
    else:
      val_list[val_list.index(item)] = ""

  #if Error is True, render index.html with the errors.
  #if Error is False, render welcome.html.
  if error == True:
    return render_template('index.html', user_error=val_list[0], pass_error=val_list[1], verify_error=val_list[2], email_error=val_list[3], username=username, email=email)
  else:
    return render_template('welcome.html', username=username)

@app.route('/welcome', methods=['POST'])
def welcome():
  username = request.form['username']

  return render_template('welcome.html', username=username)

app.run(host='0.0.0.0', port=8080)