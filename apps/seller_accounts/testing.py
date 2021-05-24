from PIL import Image
import requests

url = "http://assets.myntassets.com/v1/assets/images/2483274/2019/1/21/7d94ffc0-d1ce-4629-b300-99ead96ebcfd1548071485972-Rangriti-Women-Coral-Pink-Solid-Top-6931548071484926-1.jpg"
im = Image.open(requests.get(url, stream=True).raw)
