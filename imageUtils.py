from PIL import Image
from io import BytesIO
import requests

def getImagefromURL(url: str) -> Image:
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

def getBytesFromURL(url: str) -> BytesIO:
    response = requests.get(url)
    return BytesIO(response.content)
