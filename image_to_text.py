from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration



def img2txt(image_file):
    # Initialize the processor and model
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    

    raw_image = Image.open(image_file).convert("RGB")

    # Conditional image captioning
    text = "a photography of person wearing"  # Replace with your desired text
    inputs = processor(raw_image, text, return_tensors="pt")

    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    # Find the index of the phrase "a photography of person wearing"
    start_index = caption.find(text)

    # If the phrase is found, extract the caption from that point onward
    filtered_caption = caption[start_index + len(text):].strip()
    return filtered_caption

