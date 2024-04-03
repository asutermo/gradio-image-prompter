import gradio as gr
from gradio_image_prompter import ImagePrompter
import pandas as pd 

csv_data = []

def process_prompts(prompts):
    # Assuming prompts is a dictionary with "image" and "bbox" keys
    # For demonstration, this function simply returns what it receives.
    # You might need to adjust the logic based on what "prompts" actually contains
    # and what you want to do with it.
    _ = prompts["image"]  # This would be the image file
    bbox = prompts["bbox"][0]
    path = prompts["path"]
    df_row = [path, bbox[0], bbox[1], bbox[2], bbox[3]]
    csv_data.append(df_row)
    return [csv_data[-1]]

def export_to_csv(dataframe):
    # TODO: is this overkill?
    df = pd.DataFrame(dataframe.values)
    df.to_csv("test.csv", header=["img_path", "x0", "y0", "x1", "y1"])

with gr.Blocks() as demo:
    # Create the inputs
    with gr.Row():
        image_prompter = ImagePrompter(show_label=False)

    # Define the button to process the inputs
    append_button = gr.Button("Append Bounding Box")

    # Create the outputs
    output_bboxes_df = gr.Dataframe(label="Bounding Box", headers=["file_name", "x0", "y0", "x1", "y1"], datatype=["str", "number", "number", "number", "number"])
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
        inputs=[output_bboxes_df],
        outputs=[]
    )

    clear_button.click(lambda: [None, []], outputs=[image_prompter, output_bboxes_df])


if __name__ == "__main__":
    demo.launch()
