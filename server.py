from flask import Flask, render_template  
app = Flask(__name__)    
@app.route('/')          
def checkers():
    return render_template('index3.html', x=4, y=4, color1 = 'red', color2='black')

@app.route('/<int:y>')
def checkers_row(y):
    return render_template('index3.html', x=4, y=y, color1 = 'red', color2='black')

@app.route('/<int:x>/<int:y>')
def checkers_row2(x,y):
    return render_template('index3.html', x=x, y=y, color1 = 'red', color2='black')

@app.route('/<int:x>/<int:y>/<string:color_ichi>/<string:color_ni>')
def checkers_sensei(x,y,color_ichi,color_ni):
    return render_template('index3.html', x=x, y=y, color_ichi = color_ichi, color_ni=color_ni)

if __name__=="__main__":       
    app.run(debug=True)    

