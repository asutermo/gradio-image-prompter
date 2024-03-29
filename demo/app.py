import gradio as gr
from gradio_image_prompter import ImagePrompter

def process_prompts(prompts):
    # Assuming prompts is a dictionary with "image" and "bbox" keys
    # For demonstration, this function simply returns what it receives.
    # You might need to adjust the logic based on what "prompts" actually contains
    # and what you want to do with it.
    _ = prompts["image"]  # This would be the image file
    bbox = prompts["bbox"]   # This should be the bounding box information
    return bbox, "Export functionality to be implemented"  # Placeholder for export functionality


def extract_image_and_bbox(prompts):
    """
    Extracts the 'image' and 'bbox' values from a dictionary.

    Parameters:
    - prompts (dict): A dictionary containing various keys, including 'image' and 'bbox'.

    Returns:
    - tuple: A tuple containing the values associated with 'image' and 'bbox' keys in the input dictionary.
    """
    print(prompts)
    return prompts["image"], prompts["bbox"]

with gr.Blocks() as demo:
    # Create the inputs
    with gr.Row():
        image_prompter = ImagePrompter(show_label=False)

    # Define the button to process the inputs
    process_button = gr.Button("Process")

    # Create the outputs
    output_bbox = gr.Dataframe(label="Bounding Box", headers=["x0", "y0", "x1", "y1"])
    export_button = gr.Button("Export CSV")  # Placeholder, functionality needs to be implemented

    # Set up the interaction
    process_button.click(
        fn=process_prompts,
        inputs=image_prompter,
        outputs=[output_bbox, export_button]
    )

    # Here, you would add additional logic for what happens when `export_button` is clicked.
    # This often involves saving the processed data to a CSV file and then providing
    # that file for download. This part of the implementation is not covered in this snippet
    # because it depends on specifics about how you're handling data and what you're exporting.


if __name__ == "__main__":
    demo.launch()
