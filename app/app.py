from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Docker + EKS Project</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                margin-top: 100px;
                background: #f4f4f4;
            }

            .container {
                background: white;
                width: 600px;
                margin: auto;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 0 15px #ccc;
            }

            h1 {
                color: #333;
            }

            .success {
                color: green;
                font-size: 20px;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>🚀 Docker + Amazon EKS</h1>

            <p class="success">
                Application deployed successfully!
            </p>

            <p>
                Running inside a Docker container on Amazon EKS.
            </p>

            <p>
                DevOps Project
            </p>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
