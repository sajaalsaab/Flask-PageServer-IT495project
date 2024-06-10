__author__ = "Ziyad Alsaeed"
__email__ = "zalsaeed@qu.edu.sa"

"""
A getting started code that establish a flask app with some
predefined configuration. 

There is only one route which returns a simple text to indicate
the server is working. No malicious link or missing files handling. 
"""

import os

from flask import Flask, render_template, abort, make_response, request



app = Flask(__name__)





def is_malicious_url(url):

    forbidden_chars = ['~', '//', '..']

    for char in forbidden_chars:

        if char in url:

            return True

    return False





@app.route('/')

def hello():

    return render_template('hello.html')





@app.errorhandler(404)

def error_404(error):

    return render_template('404.html'), 404





@app.errorhandler(403)

def error_403(error):

    return render_template('403.html'), 403





@app.route('/<path:file_path>')

def serve_file(file_path):

    if is_malicious_url(file_path):

        abort(403)



    file_name = f'{file_path}.html'

    if not os.path.isfile(file_name):

        abort(404)



    with open(file_name, 'r') as file:

        content = file.read()



    response = make_response(content)

    response.headers['Content-Type'] = 'text/html'

    response.headers['Content-Disposition'] = f'attachment; filename={file_name}'

    return response





if __name__ == "__main__":

    app.run(debug=True, host='127.0.0.1')

