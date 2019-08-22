from flask import Flask, render_template, url_for, request, send_file

# Define the app
# Name the app
app = Flask(__name__)

# Articulate the routes
# index route
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/#find-me')
def showFindMe():
    return render_template('index.html#find-me')

# Run the app
if __name__ == "__main__":
    app.run()