from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

def scan_wifi():
    result = subprocess.run(['sudo', 'iwlist', 'wlan0', 'scan'], stdout=subprocess.PIPE, text=True)
    networks = set()
    for line in result.stdout.split('\n'):
        if "ESSID" in line:
            ssid = line.split(":")[1].strip().strip('"')
            if ssid:
                networks.add(ssid)
    return list(networks)

@app.route('/')
def index():
    networks = scan_wifi()
    return render_template('index.html', networks=networks)

@app.route('/connect', methods=['POST'])
def connect():
    ssid = request.form['ssid']
    password = request.form['password']
    # Use the provided SSID and password to connect to the Wi-Fi network
    # Here you can add the logic to connect to the Wi-Fi using the provided SSID and password
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
