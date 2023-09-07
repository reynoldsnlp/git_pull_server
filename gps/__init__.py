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

@app.route('/', methods=['GET'])
def root():
    with open('/tmp/gps.log', 'w') as f:
        target_dir = request.args.get('target')
        if target_dir is None:
            print(f'target_dir: {target_dir}', flush=True)
            return "No target provided", 404
        full_dir = root_dir / target_dir
        if full_dir.exists():
            with open(full_dir / 'gps.tmp', 'w') as f:
                print('gps', file=f)
            subprocess.run(['git', 'pull'], cwd=full_dir)
            return f"{target_dir} updated", 200
        else:
            return "Directory not found", 404
            print(f'full_dir: {full_dir}', flush=True)


if __name__ == '__main__':
    app.run(debug=True)
