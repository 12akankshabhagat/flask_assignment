# 4. Create a Flask app with a form that accepts user input and displays it.

from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        return render_template_string('''
            <!doctype html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>User Input Display</title>
            </head>
            <body>
                <h1>You entered: {{ user_input }}</h1>
                <a href="/">Go back</a>
            </body>
            </html>
        ''', user_input=user_input)
    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Enter User Input</title>
        </head>
        <body>
            <h1>Enter some text</h1>
            <form method="post">
                <input type="text" name="user_input" required>
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(host="0.0.0.0" , port=5001)

