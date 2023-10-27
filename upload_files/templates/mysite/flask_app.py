from flask import Flask, render_template, request
import subprocess
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('terminal.html')
@app.route('/execute', methods=['POST'])
def execute():
    command = request.form['command']
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        output = e.output
    output = output.decode()
    return render_template('terminal.html', output=output)
if __name__ == '__main__':
    app.run()
