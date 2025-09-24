# 代码生成时间: 2025-09-24 08:59:50
import gradio as gr
def add(a, b):
    """Add two numbers"""
    return a + b
def subtract(a, b):
    """Subtract two numbers"""
    return a - b
def multiply(a, b):
    """Multiply two numbers"""
    return a * b
def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
def main():
    """Main function to create the Gradio interface"""
    # Create the Gradio interface
    with gr.Blocks() as demo:
        # Input for addition
        with gr.Row():
            add_input1 = gr.Number(label="Number 1")
            add_input2 = gr.Number(label="Number 2")
            add_output = gr.Number(label="Result")
        # Button for addition
        add_button = gr.Button("Add")
        # Output for addition
        gr.Markdown("## Addition")
        add_button.click(fn=add, inputs=[add_input1, add_input2], outputs=add_output)

        # Input for subtraction
        with gr.Row():
            sub_input1 = gr.Number(label="Number 1")
            sub_input2 = gr.Number(label="Number 2")
            sub_output = gr.Number(label="Result")
        # Button for subtraction
        sub_button = gr.Button("Subtract")
        # Output for subtraction
        gr.Markdown("## Subtraction")
        sub_button.click(fn=subtract, inputs=[sub_input1, sub_input2], outputs=sub_output)

        # Input for multiplication
        with gr.Row():
            mul_input1 = gr.Number(label="Number 1")
            mul_input2 = gr.Number(label="Number 2")
            mul_output = gr.Number(label="Result")
        # Button for multiplication
        mul_button = gr.Button("Multiply")
        # Output for multiplication
        gr.Markdown("## Multiplication")
        mul_button.click(fn=multiply, inputs=[mul_input1, mul_input2], outputs=mul_output)

        # Input for division
        with gr.Row():
            div_input1 = gr.Number(label="Number 1")
            div_input2 = gr.Number(label="Number 2")
            div_output = gr.Number(label="Result")
        # Button for division
        div_button = gr.Button("Divide")
        # Output for division
        gr.Markdown("## Division")
        div_button.click(fn=divide, inputs=[div_input1, div_input2], outputs=div_output)

    # Launch the interface
    demo.launch()

# Call the main function to launch the interface
if __name__ == "__main__":
    main()