from os import path
import pickle
import mysql.connector
from datetime import date, timedelta
from passlib.hash import django_pbkdf2_sha256


class User(object):
    def __init__(self, firstname="", lastname="", email=None, paid_until=None, is_logged_in=False):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.paid_until = paid_until
        self.is_logged_in = is_logged_in
        self.session_expire_date = None

        if path.isfile('user.dat'):
            with open('user.dat', 'rb') as f:
                self.firstname, self.lastname, self.email, self.paid_until, self.is_logged_in, self.session_expire_date = pickle.load(f)

        # print(self.firstname + " " + self.lastname + " " + self.email)

        # Set attributes for firstname, lastname, email, paid_until.
        # Make all attributes None if no arguments are given.
        # firstname, lastname, email should be string.
        # paid_until should be datetime type.

    def is_subscribed(self):
        today = date.today()

        if self.paid_until is None:
            return False

        if today < self.paid_until:
            return True
        else:
            return False
        # Return boolean
        # Check if the user is subscribed to Script Spinner.
        # if today < paid_until: return True, else return False

    def getFullname(self):
        return (self.firstname + " " + self.lastname)
        # Return string
        # Get user fullname.

    def login(self, email, password, remember):
        mydb = mysql.connector.connect(
        host="45.63.10.63",
        user="scriptspinner-tester",
        password="TyQA6f%2xm]L7,mrLNJqL.#hvXL=4L",
        database="scriptspinner-test",
        port="3306"
        )

        mycursor = mydb.cursor(buffered=True)

        mycursor.execute("""
            SELECT
                *
            FROM
                user_scriptspinneruser
            WHERE
                email = %(email)s
        """, {
            'email': email
        })

        user = mycursor.fetchone()

        if user and django_pbkdf2_sha256.verify(password, user[1]):
            self.is_logged_in = True
            self.firstname = user[4]
            self.lastname = user[5]
            self.email = user[9]
            self.paid_until = [10]

            if remember:
                self._remember()

            return True
        else:
            return False

        # Check if user.dat exist. If not,
        # Access the database and authenticate the user.
        # if email and password are valid, retrieve information from database
        # then set all attributes.
        # if remember is True, call _remeber function.
        # if email and password are not valid, raise UserNotFoundException

    def logout(self):
        with open('user.dat', 'w'):
            pass
        # Delete the contents of user.dat

    def _remember(self, json=None):
        self._set_session_expire_date()
        with open("user.dat", 'wb') as f:
            pickle.dump([self.firstname, self.lastname, self.email, self.paid_until, self.is_logged_in, self.session_expire_date], f)

        # Create user.dat then store user information on user,dat file.
        # Save it as JSON format.

    def _set_session_expire_date(self):
        self.session_expire_date = date.today() + timedelta(days=31)
        # Set session expire date. It should be 30 days ahead from today.

    def _update_last_login(self):
        pass
        # Update Last Login date on the database.
        # This function is less important. Don't spend too much time on this.


if __name__ == '__main__':
    user = User()
    # print(user.login('user@scriptspinner.com', 'pass123word', True))
    # Create a user class object with no argument.
    # Create a user class object with arguments.
    # Print users full name.