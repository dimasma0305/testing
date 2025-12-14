
import os
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        # Backend is reachable via 'backend' hostname or 'localhost' depending on Nomad network mode.
        # If we use native Nomad bridge, they are in the same group, so localhost should work.
        # But if standard docker-compose is simulated via raw_exec or podman, it might be different.
        # For our "nomad_generator.go", if services are > 1, it uses `generateDockerComposeJob` with `raw_exec`.
        # This implies standard docker-compose networking where services are reachable by name.
        r = requests.get('http://backend:5000/secret', timeout=2)
        return f"Frontend here! The backend says: {r.text}"
    except Exception as e:
        return f"Frontend here! Failed to contact backend: {str(e)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
