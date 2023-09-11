"""Flask webapp to trigger a `git pull`."""

import os
import os.path
from pathlib import Path
import subprocess

from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)

local_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = Path(os.environ.get('GPS_ROOT_DIR', '')).resolve()
print(f'Root directory (GPS_ROOT_DIR): {root_dir}', flush=True)

for each_dir in root_dir.iterdir():
    print(subprocess.run(['git', 'config', '--global', '--add', 'safe.directory', str(each_dir.resolve())]), flush=True)

@app.route('/', methods=['GET'])
def root():
    with open('/tmp/gps.log', 'w') as f:
        target_dir = request.args.get('target')
        if target_dir is None:
            print(f'No target provided', flush=True)
            return "No target provided\n", 404
        full_dir = root_dir / target_dir
        if full_dir.exists():
            subprocess.run(['git', 'pull'], cwd=full_dir)
            return f"{target_dir} updated\n", 200
        else:
            print(f'Directory not found: {target_dir}', flush=True)
            return "Directory not found\n", 404


if __name__ == '__main__':
    app.run(debug=True)
