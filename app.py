from flask import Flask, render_template, url_for, request

# Name the app
app = Flask(__name__)

# Articulate the routes
# index route
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/dog-merch/')
def showDogMerch():
    items = request.query_string
    cardholder_fields = [
        ('name',
         'Dog Love'),
        ('address',
         '420 Dogg Ave'),
        ('city',
         'Poochy'),
        ('state',
         'CA'),
        ('zip',
         '94110'),
        ('email',
         'dogs@sydney-and-sesil.com')]
    return render_template('dog-merch.html',
                           #session_data=session,
                           cardholder_fields=cardholder_fields,
                           items=items,
                           cart_headline_image_url='')

@app.route('/#find-me')
def showFindMe():
    return render_template('index.html#find-me')

@app.route('/terms')
def showTerms():
    return render_template('terms.html')

@app.route('/success')
def showSuccess():
    return render_template('success.html')

@app.route('/failure')
def showFailure():
    return render_template('failure.html')


# Run the app
if __name__ == "__main__":
    app.run()