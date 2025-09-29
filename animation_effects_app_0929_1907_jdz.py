# 代码生成时间: 2025-09-29 19:07:16
import gradio as gr
def animate(effect, duration):
    """
    Animates the provided effect over the specified duration.
    
    Args:
        effect (str): The type of animation effect to be applied.
        duration (int): The duration of the animation in seconds.
    
    Returns:
        str: A success message indicating the animation effect and duration.
    
    Raises:
        ValueError: If the effect is not recognized or the duration is invalid.
    """
    # Define a dictionary of supported animation effects
    animations = {"slide": 1, "fade": 2, "zoom": 3}
    
    # Check if the effect is supported
    if effect not in animations:
        raise ValueError("Unsupported animation effect. Please choose from: slide, fade, zoom.")
    
    # Check if the duration is a positive integer
    if not isinstance(duration, int) or duration <= 0:
        raise ValueError("Duration must be a positive integer.")
    
    # Simulate animation (this is where actual animation logic would be implemented)
    # For demonstration purposes, we just return a success message
    return f"Animation '{effect}' performed for {duration} seconds."

# Create a Gradio interface
iface = gr.Interface(
    animate,
    inputs=["text",  1], 
    outputs="text")

# Launch the Gradio app
iface.launch()