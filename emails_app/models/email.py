import re	# the regex modulefrom flask import flash
from flask import flash
from emails_app.config.mysqlconnection import connectToMySQL
from datetime import datetime
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self,data):
            self.id = data['id']
            self.address = data['address']
            self.created_at = data['created_at'].strftime("%B %d , %Y, %H:%M:%S")
            self.updated_at = data['updated_at']


    @classmethod
    def save(cls,data):
        query = "Insert INTO emails (address,created_at,updated_at) VALUES(%(address)s,NOW(),NOW());"
        my_email= connectToMySQL('email').query_db(query,data) # this produces a number for the last row
        print("****************************************************************************************")
        print(my_email)
        return my_email

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results= connectToMySQL('email').query_db(query)
        print("------------------------------------------------------------------------------------------------------------------------------------------")
        print(results) ## this is a list of dictionaries in emails
        emails= [] ## this is an object
        for email in results:
            emails.append(cls(email))
        print("///////////////////////////////////////////////////////////////////////////////////////////")
        print(emails)
        return emails


    @staticmethod
    def validate_user( data ):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(data['address']): 
            flash("Invalid email address!")
            is_valid = False

        if is_valid == False:
            return is_valid
        elif is_valid == True:
            flash ("Success!")
            
            return is_valid

