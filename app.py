from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    final_grade = None
    final_gpa = None
    if request.method == 'POST':
        current_grade = request.form['current_grade']
        desired_percentage = request.form['percentage']
        final_weight = request.form['weight']
        if final_weight == "0" or final_grade == "":
            return render_template('index.html', final_grade = "Cannot Divide by zero")
        try:
            final_grade = final_grade_calculation(float(current_grade), float(desired_percentage), float(final_weight))
        except ValueError:
            final_grade = "Invalid inputs, please enter numbers"
    if final_grade == None or final_grade == "":
        return render_template('index.html', final_grade = "")

    return render_template('index.html', final_grade = "You need a " + str(round(float(final_grade), 2))+ " on your final")



def final_grade_calculation(current_grade: int, desired_percentage: int, final_weight: int) -> float:
    result = (desired_percentage - current_grade * (100 - final_weight)/100)/(final_weight/100)
    return result

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    
