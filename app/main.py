import os

from fastapi import FastAPI, File, UploadFile
from efficientnet_pytorch import EfficientNet
from PIL import Image
import torchvision.transforms as transforms
import torch.nn as nn
from configurations import id2label
import uvicorn
import torch

model = None
image_dir = "images/"
app = FastAPI()


@app.on_event("startup")
def startup_event():
    global model
    model = EfficientNet.from_name('efficientnet-b2')
    model._fc = nn.Linear(model._fc.in_features, 101)
    model.load_state_dict(
        torch.load('model/efficientnet_b2_20_epochs.pt',
                   map_location=torch.device('cuda' if torch.cuda.is_available() else 'cpu')))
    model.eval()

    if 'images' not in os.listdir('.'):
        os.mkdir(image_dir)


@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()

    with open(f"{image_dir}{file.filename}", "wb") as f:
        f.write(contents)

    try:
        image = Image.open(f"{image_dir}{file.filename}")
    except:
        return {'message': 'this file is not an image'}

    transform = transforms.Compose([
        transforms.PILToTensor(),
        transforms.Resize((256, 256))
    ])
    img_tensor = transform(image)

    try:
        ids = model(img_tensor.unsqueeze(0).float())
        id = torch.argmax(ids).item()
        label = id2label[id]
    except RuntimeError:
        return {'message': 'error',
                'description':
                    'this photo seems to have no instances of food on it'}
    except KeyError:
        return {'message': 'error',
                'description': 'this image seems to have no instances of food on it'}

    return {
        "message": "success",
        "filename": file.filename,
        "class_label": label}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
