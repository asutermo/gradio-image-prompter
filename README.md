# Image Prompter for Gradio

A gradio component to draw a bounding box and get the coordinates to export to CSV.

## Installation

### Preliminaries

``gradio`` >= 4.0.0

### Installing Package

```bash
pip install gradio-image-prompter
```

## Quick Start

### Development

```bash
cd gradio-image-prompter
gradio cc install
gradio cc dev
```

### Example

```python
import gradio as gr
from gradio_image_prompter import ImagePrompter

demo = gr.Interface(
    lambda prompts: (prompts["image"], prompts["bbox"]),
    ImagePrompter(show_label=False),
    [gr.Image(show_label=False), gr.Dataframe(label="Bounding Box")],
)
demo.launch()

```

## License
[Apache License 2.0](LICENSE)

## Acknowledgement

We thank the repositories: [gradio-image-prompter](https://github.com/PhyscalX/gradio-image-prompter) and [Gradio](https://github.com/gradio-app/gradio).
