from emails_app import app
from flask import render_template,redirect,request,session,flash
from emails_app.models.email import Email


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    if not Email.validate_user(request.form):
        # we redirect to the template with the form.
        return redirect('/')
    # ... do other things
    data = {
        "address": request.form['address']
    }
    email_id = Email.save(data)

    return redirect('/success')
    # else no errors:

@app.route('/success')
def success():
    # data = {
    # "address" : session['address']
    # }
    returned_object = Email.get_all() 
    return render_template("success.html", results = returned_object)
    

@app.route('/delete')
def delete(user_id):
    data = {
        "id" : user_id
    }
    # We pass the data dictionary into the save method from the User class.
    Email.delete(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')