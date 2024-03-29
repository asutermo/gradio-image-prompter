import gradio as gr
from gradio_image_prompter import ImagePrompter

bounding_boxes = []

def process_prompts(prompts):
    # Assuming prompts is a dictionary with "image" and "bbox" keys
    # For demonstration, this function simply returns what it receives.
    # You might need to adjust the logic based on what "prompts" actually contains
    # and what you want to do with it.
    _ = prompts["image"]  # This would be the image file
    #bbox = prompts["bbox"]   # This should be the bounding box information
    bounding_boxes.append(prompts["bbox"])
    return bounding_boxes[-1]  # Placeholder for export functionality

def export_to_csv():
    with open('test.csv', 'w') as csv:
        csv.write('woo')

def extract_image_and_bbox(prompts):
    """
    Extracts the 'image' and 'bbox' values from a dictionary.

    Parameters:
    - prompts (dict): A dictionary containing various keys, including 'image' and 'bbox'.

    Returns:
    - tuple: A tuple containing the values associated with 'image' and 'bbox' keys in the input dictionary.
    """
    return prompts["image"], prompts["bbox"]


with gr.Blocks() as demo:
    # Create the inputs
    with gr.Row():
        image_prompter = ImagePrompter(show_label=False)

    # Define the button to process the inputs
    append_button = gr.Button("Append Bounding Box")

    # Create the outputs
    output_bboxes_df = gr.Dataframe(label="Bounding Box", headers=["x0", "y0", "x1", "y1"])
    clear_button = gr.ClearButton()
    export_button = gr.Button("Export CSV")  # Placeholder, functionality needs to be implemented

    # Set up the interaction
    append_button.click(
        fn=process_prompts,
        inputs=image_prompter,
        outputs=[output_bboxes_df]
    )

    export_button.click(
        fn=export_to_csv,
        inputs=[],
        outputs=[]
    )

    clear_button.click(lambda: [None, []], outputs=[image_prompter, output_bboxes_df])


if __name__ == "__main__":
    demo.launch()
