from application import app

# Main method that lets us use python 'app.name' in terminal to run the
# the application in debug mode.
if __name__ == '__main__':
    app.run(debug=True)
