from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'


@app.route('/some_route')
def some_route():
    # Access the secret key
    secret_key = app.secret_key

    # Do something with the secret key
    return 'Secret Key: {}'.format(secret_key)

app.run()