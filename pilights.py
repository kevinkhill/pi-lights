from flask import (
    Flask,
    render_template as template,
    redirect
)
import relay

app = Flask(__name__)
relay.init()

@app.route('/')
def index():
    return template('index.html')

@app.route('/lights/on')
def lights_on():
    relay.on()
    return redirect('/')

@app.route('/lights/off')
def lights_off():
    relay.off()
    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)
