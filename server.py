from flask import Flask, render_template

app = Flask(__name__)

# Render basic board 8 by 8, colors red and black
@app.route('/')
def create_board():
    return render_template('index.html', num1=8, num2=8, color1='red', color2='black')

# Change number of rows
@app.route('/<int:num1>')
def create_board_row(num1):
    return render_template('index.html', num1=num1, num2=8, color1='red', color2='black')

# change number of rows and columns
@app.route('/<int:num1>/<int:num2>')
def create_board_row_column(num1, num2):
    return render_template('index.html', num1=num1, num2=num2, color1='red', color2='black')

# change number of rows, columns and 1 color
@app.route('/<int:num1>/<int:num2>/<string:color1>')
def create_board_row_column_color1(num1, num2, color1):
    return render_template('index.html', num1=num1, num2=num2, color1=color1, color2='black')

# change number of rows, column and both colors of board
@app.route('/<int:num1>/<int:num2>/<string:color1>/<string:color2>')
def create_board_row_column_color1_color2(num1, num2, color1, color2):
    return render_template('index.html', num1=num1, num2=num2, color1=color1, color2=color2)

# Error message for 404
@app.errorhandler(404)
def page_not_found(e):
    return f'Sorry! No response. Try again'

# Ensure this file is being run directly and not from different
# module and run on port 5001 for mac
if __name__=="__main__":
    app.run(host='localhost', port=5001, debug=True)
