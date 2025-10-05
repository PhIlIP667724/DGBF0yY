# 代码生成时间: 2025-10-06 01:40:24
import gradio as gr
def recognize_image(image_path):
    """
    Recognize the content of an image using pre-trained models.
    :param image_path: Path to the image file.
    :return: A list of recognized objects in the image.
    """
    # You can replace this with your preferred model loading code
    from PIL import Image
    import torch
    from torchvision import models, transforms
    
    # Load a pre-trained model for image recognition
    model = models.resnet50(pretrained=True)
    model.eval()
    
    # Define transformations
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    
    try:
        # Open the image
        with Image.open(image_path) as img:
            img = transform(img).unsqueeze(0)
            # Forward pass
            outputs = model(img)
            # Get predicted class
            _, predicted_class = torch.max(outputs, 1)
            return f"Predicted class: {predicted_class.item()}"
    except Exception as e:
        # Handle exceptions, such as file not found or invalid image format
        return f"Error processing the image: {e}"

# Create Gradio interface
iface = gr.Interface(
    fn=recognize_image,
    inputs=gr.inputs.Image(label="Upload an image"),
    outputs="text",
    title="Image Recognition App",
    description="Upload an image to recognize objects.",
)

# Launch the app
iface.launch()