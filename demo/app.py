import gradio as gr
from gradio_image_prompter import ImagePrompter

demo = gr.Interface(
    lambda prompts: (prompts["image"], prompts["bbox"]),
    ImagePrompter(show_label=False),
    [gr.Image(show_label=False), gr.Dataframe(label="Bounding Box")],
)
demo.launch()
