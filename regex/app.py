from flask import Flask, request, render_template, jsonify
import re

app = Flask(__name__)
##################################
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form.get('test_string')
    regex_pattern = request.form.get('regex_pattern')
    
    # Perform regex matching
    matched_strings = re.findall(regex_pattern, test_string)

    return render_template('index.html', test_string=test_string, regex_pattern=regex_pattern, matched_strings=matched_strings)

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form.get('email')

    # Perform email validation using a simple regex pattern
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    is_valid_email = re.match(email_pattern, email) is not None

    # Return a JSON response indicating whether the email is valid
    return jsonify({'is_valid_email': is_valid_email})
##################################

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000)