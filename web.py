import launch
from flask import Flask, request, jsonify
import sys, os, subprocess, time, re, json, urllib.request, urllib.error, shutil, tempfile, zipfile, io
from contextlib import redirect_stdout

app = Flask(__name__)

def capture_output(fpf):

    buffer = io.StringIO()

    with redirect_stdout(buffer):
        launch.launch(fpf)
        

    terminal_output = buffer.getvalue()
    return terminal_output

@app.route('/tool/<choice>', methods=['GET'])
def run_tool(choice):
    star_tools = launch.scan_folder(launch.STAR_DIR, is_star=True)
    free_tools = launch.scan_folder(launch.TOOLS_DIR, is_star=False)
    all_tools  = star_tools + free_tools

    star_ok     = launch._check_star_github()
    total       = len(all_tools)
    total_pages = max(1, (total - 1) // launch.ITEMS_PER_PAGE + 1)
    # page        = max(1, min(page, total_pages))

    # start      = (page - 1) * launch.ITEMS_PER_PAGE
    # page_tools = all_tools[start:start + launch.ITEMS_PER_PAGE]


    n = int(choice)
    if 1 <= n <= total:
        fp, is_star_tool = all_tools[n - 1]
        if is_star_tool and not star_ok:
            launch.show_star_tutorial()
        else:
            capture_output(fp)
    else:
        launch.err(launch.t('invalid')); time.sleep(0.4)

if __name__ == "__main__":
    app.run(debug=True, port=8080) #change port to env later
