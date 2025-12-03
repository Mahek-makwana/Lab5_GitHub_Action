from flask import Flask, render_template_string

# Create the Flask application instance
app = Flask(__name__)

# Define the HTML template for the greeting page
GREETING_HTML = """
<!doctype html>
<title>Greeting Page</title>
<h1>Hello World! Welcome to the Automation Lab.</h1>
"""

# The root route (/) is intentionally left undefined/not handled
# to produce the 404 error mentioned in the lab instruction.

# Define the '/greeting' route
@app.route('/greeting')
def greeting():
    # Renders the HTML template when accessing /greeting
    return render_template_string(GREETING_HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)