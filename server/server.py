from flask import Flask, request, send_file
from imageGenerator import concatenate_sentence_images
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins="*")

@app.route('/', methods=['POST'])
def handle_post_request():
    # Access the request data
    data = request.get_json()
    sentence = data['testo']


    # Generate the image
    image = concatenate_sentence_images(sentence)
    image_path = 'temp_image.png'
    image.save(image_path)

    # Return the image file as the response
    # return "Message received"
    return send_file(image_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(port=2700)
