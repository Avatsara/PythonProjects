from flask import Flask
import os
import datetime
import subprocess
import pytz

app = Flask(__name__)

@app.route("/htop")
def htop():
    name = "Arpan Tiwari"  
    username = os.getenv("USER") or os.getenv("USERNAME")  
    ist = pytz.timezone("Asia/Kolkata")
    server_time = datetime.datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %Z")
    
    # Get top command output
    try:
        top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode("utf-8")
    except Exception as e:
        top_output = f"Error fetching top output: {str(e)}"
    
    response = f"""
    <html>
    <head><title>/htop</title></head>
    <body>
        <h1>System Information</h1>
        <p><b>Name:</b> {name}</p>
        <p><b>Username:</b> {username}</p>
        <p><b>Server Time (IST):</b> {server_time}</p>
        <h2>Top Output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)