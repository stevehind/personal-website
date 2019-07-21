from flask import Flask, render_template, url_for

# Name the app
app = Flask(__name__)

# Articulate the routes
# index route
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/dog-merch/')
def showDogMerch():
    return render_template('dog-merch.html')

@app.route('/#find-me')
def showFindMe():
    return render_template('index.html#find-me')

@app.route('/terms')
def showTerms():
    return render_template('terms.html')

# Run the app
if __name__ == "__main__":
    app.run()