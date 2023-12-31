import sys

import converter
from flask_cors import CORS
from flask import Flask, render_template, request, send_file


app = Flask(__name__)
CORS(app)


@app.route('/')
def main_page():
    return render_template('upload.html')


@app.route('/<string:page_name>')
def upload_file(page_name=None):
    return render_template(page_name)


# @app.route('/download')
# def file_downloads():
#     try:
#         return render_template('download.html')
#     except Exception as e:
#         return str(e)


@app.route('/converted', methods=['POST', 'GET'])
def convert():
    if request.method == 'POST':
        try:
            converter.create_dir()

            csv_filename = 'temp/uploaded-file.csv'
            json_filename = 'temp/uploaded-file.json'

            print(request.files.get('file'), file=sys.stderr)
            f = request.form['file']

            print('OK!!!', file=sys.stderr)

            print(f)

            f.save(csv_filename)
            converter.csv_to_json(csv_filename, json_filename)

            return send_file(json_filename)
        except Exception as err:
            return f'There was a problem with saving {err}'
        finally:
            converter.remove_dir()


if __name__ == '__main__':
    app.run()
