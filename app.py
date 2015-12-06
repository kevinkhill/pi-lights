from flask import (
    Flask,
    render_template as template,
    redirect
)
import relay

app = Flask(__name__)
routes = dict(
    root='/',
    lights_on='/lights/on',
    lights_off='/lights/off'
)

@app.route(routes['root'])
def index():
    return template('index.html', urls=dict(
        lights_on=routes['lights_on'],
        lights_off=routes['lights_off']
    ))

@app.route(routes['lights_on'])
def lights_on():
    relay.on()
    return redirect('/')

@app.route(routes['lights_off'])
def lights_off():
    relay.off()
    return redirect('/')

if __name__ == "__main__":
    relay.init()
    app.run(host='192.168.0.123', port=80, debug=True, use_reloader=True)
