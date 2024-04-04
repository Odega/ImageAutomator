from flask import Flask, render_template, request
from langchain_community.llms import Ollama
import ollama
from ollama import generate
from prompts import llava_prompt
import json
import os
import shutil
from werkzeug.utils import secure_filename

import glob

#for multimodal
import base64
from io import BytesIO
#from IPython.display import HTML, display
from PIL import Image

app = Flask(__name__)
llm = Ollama(model="llava")

# Set the directory where uploaded images will be saved
UPLOAD_FOLDER = './static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

          # Handle image upload
        images = request.files.getlist('images')
        image_filenames = []
        for image in images:
            filename = secure_filename(image.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(image_path)
            image_filenames.append(filename)

        # Process the description and extract information
        jsons=[]
        for image_file in images:
            jsons.append(process_image(image_file))

        print("********************************************")

        parsed_data = []
        for item in jsons:
            json_string = item.strip().strip('```json').strip()
            parsed_item = json.loads(json_string)
            if isinstance(parsed_item, list):
                parsed_data.extend(parsed_item)
            else:
                parsed_data.append(parsed_item)

        print(parsed_data)
        item=parsed_data
        print("***")    
        print("k")
        # Combine data and image filenames
        combined_data = zip(parsed_data, image_filenames)

        return render_template('index.html', combined_data=combined_data)

        #return render_template('index.html', data=parsed_data, image_paths=image_paths)
    return render_template('index.html')

# processing the images 
def process_image(image_file):
    print(f"\nProcessing {image_file}\n")
    with Image.open(image_file) as img:
        with BytesIO() as buffer:
            img.save(buffer, format='PNG')
            image_bytes = buffer.getvalue()

    full_response = ''
    # Generate a description of the image
    for response in generate(model='llava', 
                             prompt=llava_prompt,
                             images=[image_bytes], 
                             stream=True):
        # Print the response to the console and add it to the full response
        #print(response['response'], end='', flush=True)
        full_response += response['response']
    return full_response 

if __name__ == '__main__':
    app.run()