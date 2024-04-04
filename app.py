from flask import Flask, render_template, request, flash, redirect
from prompts import claude_haiku_prompt
import json
import os
from dotenv import load_dotenv
import shutil
from werkzeug.utils import secure_filename
from PIL import Image

import anthropic
import os
import base64
import httpx


import glob
load_dotenv() 
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 2 Megabytes
MAX_FILE_UPLOADS = 4  # Max number of files per upload

client = anthropic.Anthropic(
    api_key = os.getenv("anthropic_key"),
)   
# Choose model (llm_model)
sonnet_model = "claude-3-sonnet-20240229"
haiku_model = "claude-3-haiku-20240307"
llm_model = haiku_model

# Set the directory where uploaded images will be saved
UPLOAD_FOLDER = './static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#selected_language = ""
@app.route('/', methods=['GET', 'POST'])
def index():
    combined_data = []
    if request.method == 'POST':
        #selected_language = request.form['language']
        #print(selected_language)
        images = request.files.getlist('images')
        print("*** Images ***")
        print(images)
        print("**********************************")
        if len(images) > MAX_FILE_UPLOADS:
            return "No more than 4 images", 400
        for image in images:
            filename = secure_filename(image.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(image_path)

            print("********* create_haiku_task **************")
            file_ext = os.path.splitext(filename)[1][1:]

            # Process each image with Haiku
            haiku_response = create_haiku_task(image_path, file_ext)
            print("********* haiku_response **************")
            print(haiku_response)
            print("**********************************")
            # Given the structure of your response, extracting and parsing the JSON string
            analysis_results_string = haiku_response.content[0].text
            try:
                analysis_results = json.loads(analysis_results_string)
                print("********* analysis_results **************")
                print(analysis_results)
                print("**********************************")

                # For each result in analysis_results, append a tuple of the result and the image filename to combined_data
                for result in analysis_results:
                    combined_data.append((result, filename))
            except ValueError as e:
                print("XXXXXX Value error XXXXX")
                print(e)
            except:
                print("XXXX OTHER EXCEPT XXXX")
            

    # Render your template with the combined data
    return render_template('index.html', combined_data=combined_data)

def create_haiku_task(image_path,ext):
    with open(image_path, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode("utf-8")
    print("**ADADADA***")
    print(ext)

    custom_prompt = claude_haiku_prompt

    image_media_type = f"image/{ext}"  # Adjust based on your image format
    #IF image jpg -> make png
    if ext == "jpg":
        print(image_path)
        print("Image in jpg -> converting to jpeg")

        jpeg_path = image_path.rsplit('.', 1)[0] + '.jpeg'
        # Open and save the image to change its extension
        with Image.open(image_path) as img:
            img.save(jpeg_path)
        
        # Correctly encode the newly saved jpeg image to base64
        with open(jpeg_path, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode("utf-8")
        
        print(f"*** Saved to {jpeg_path} ***")

        # Assuming 'client' is already configured for your Anthropic API
        response = client.messages.create(
            model=llm_model,
            max_tokens=1024,
            #system=f"Respond only in {selected_language}.",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/jpeg",
                                "data": image_data,
                            },
                        },
                        {
                            "type": "text",
                            "text": custom_prompt
                        }
                    ],
                }
            ],
        )
        return response
    else:
        
        # Assuming 'client' is already configured for your Anthropic API
        response = client.messages.create(
            model=llm_model,
            max_tokens=1024,
            #system=f"Respond only in {selected_language}.",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": image_media_type,
                                "data": image_data,
                            },
                        },
                        {
                            "type": "text",
                            "text": custom_prompt
                        }
                    ],
                }
            ],
        )
        return response 

if __name__ == '__main__':
    app.run()