from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def create_board():
    return render_template('index.html', num=4, color='white')

# Error message for 404
@app.errorhandler(404)
def page_not_found(e):
    return f'Sorry! No response. Try again'

# Ensure this file is being run directly and not from different
# module and run on port 5001 for mac
if __name__=="__main__":
    app.run(host='localhost', port=5001, debug=True)