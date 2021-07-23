from flask import Flask, render_template, request, redirect, session
from emails_app.controllers import emails
from emails_app import app

# Always needed
if __name__=="__main__":   
    app.run(debug=True)    

