# Final-Grade-Calculator
Program designed using Flask and calculates the grade you need on your final to achieve the desired class percentage
---
## Running the application

Must have python installed (visit [python](https://www.python.org/downloads/))

Check if pip is installed
```sh
pip --verison
```

Install Flask
```sh
pip install Flask
```

Run the application
```sh
python app.py
```

Navigate to http://127.0.0.1:5000/

---
## How it works
Grade needed = (desired percentage - current grade * (100 - final weight)/100)/(final weight/100)

---
## Inspiration
[Roger Hub's](https://rogerhub.com/final-grade-calculator/) Final Grade Calculator

