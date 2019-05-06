# Copyright 2019 The crowdcompute:face-reco-app Authors
# This file is part of the crowdcompute:face-reco-app library.
#
# The crowdcompute:face-reco-app library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# The crowdcompute:face-reco-app library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with the crowdcompute:face-reco-app library. If not, see <http://www.gnu.org/licenses/>.

import os
import imagehash
import numpy as np
from PIL import Image
import face_recognition as fr
from werkzeug.utils import secure_filename
from flask import Flask, abort, request, jsonify, send_from_directory

APP_ROOT = "/"
FACES_DIR = os.path.join(APP_ROOT, 'faces')
if not os.path.isdir(FACES_DIR):
    os.mkdir(FACES_DIR)
api = Flask(__name__)

@api.route('/download/<path:filename>')
def static_files(filename):
    """Download a file."""
    return send_from_directory(FACES_DIR, filename, as_attachment=True)

@api.route('/face_reco', methods=['GET', 'POST'])
def upload():
    json_urls = {}
    if request.method == 'POST':
        for image_bytes in request.files.getlist('images'):
            if not file_check(image_bytes):
                return 'Uploaded files are not supported...'
            image = Image.open(image_bytes)
            face_urls = face_recognize(image)
            json_urls[image_bytes.filename] = face_urls
    return jsonify(json_urls)

def file_check(img):
    filename = img.filename
    # Secure a filename before storing it
    filename = secure_filename(filename)
    # Verify file is supported
    ext = os.path.splitext(filename)[1][1:].strip().lower()
    if ext in set(['jpg', 'jpeg', 'png']):
        print('File supported moving on...')
        return True
    else:
        return False

# Cut the faces from the picture
def cut_face(image, face_location):
    top, right, bottom, left = face_location
    face_pixels = image[top:bottom, left:right]
    return Image.fromarray(face_pixels)

def face_recognize(img):
    face_urls = []
    print("Result will be saved at {0}".format(FACES_DIR))
    image = np.array(img)
    face_locations = fr.face_locations(image)

    print("There are {} face(s) in this photograph.".format(len(face_locations)))
    for face_location in face_locations:
        face_image = cut_face(image, face_location)
        hash = imagehash.average_hash(face_image)
        face_filename = "face_" + str(hash) + ".bmp"
        # Save the image
        face_image.save(os.path.join(FACES_DIR, face_filename))
        face_urls.append('{0}download/{1}'.format(request.url_root, face_filename))
    return face_urls

if __name__ == "__main__":
    api.run(host="0.0.0.0", port=3000)