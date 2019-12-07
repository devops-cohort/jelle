from application import app

#runs in the debug mode and allows for connections from all IPs
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
