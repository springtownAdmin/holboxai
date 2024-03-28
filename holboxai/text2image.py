import base64
import json
import logging
import boto3
import io
from PIL import Image
from botocore.exceptions import ClientError

class text2image:
    
    def __init__(self):
        self.client = boto3.client('bedrock-runtime')
        
    def generate_image(self,prompt,cfg_scale=10, steps=50):
        try:
            body = json.dumps({
                        "text_prompts": [{"text": prompt}],
                        "seed": 10,
                        "cfg_scale": cfg_scale,
                        "steps": steps,
                    })
            response = self.client.invoke_model(
                        modelId="stability.stable-diffusion-xl-v1",
                        accept = "application/json",
                        contentType="application/json",
                        body=body
                    )   
            response_body = json.loads(response.get("body").read())
            base64_image = response_body.get("artifacts")[0].get("base64")
            base64_bytes = base64_image.encode('ascii')
            image_bytes = base64.b64decode(base64_bytes)
            image = Image.open(io.BytesIO(image_bytes))
            image.save("./image.jpg") 
            print("image saved to path :  /image.jpg")
        except ClientError as e:
            logging.error("A client error occured: %s", e)
            return None 
    
         