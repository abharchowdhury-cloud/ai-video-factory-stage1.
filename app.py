
import gradio as gr
from datetime import datetime

def create_plan(topic, audience, duration):
    topic = topic.strip()
    if not topic:
        return "Please enter a video topic."

    return f"""# AI Video Factory — Production Plan

Topic: {topic}
Audience: {audience}
Duration: {duration} minutes
Created: {datetime.now().strftime('%Y-%m-%d')}

## Suggested YouTube Title
{topic}: Beginner's Guide and Practical Tutorial

## SEO Keywords
{topic}, AI tools, software tutorial, how to use {topic}

## Video Structure
00:00 — Original introduction and hook
00:30 — Explain the problem
01:30 — Introduce the software
03:00 — Step-by-step demonstration
05:30 — Practical example
07:00 — Common mistakes and tips
08:00 — Summary and conclusion

Adjust timestamps to match the selected duration.

## Production Checklist
[ ] Research and verify all claims
[ ] Write an original script
[ ] Record or license visuals
[ ] Verify music and image rights
[ ] Produce voice-over
[ ] Edit and add subtitles
[ ] Create an original thumbnail
[ ] Review copyright and accuracy
[ ] Obtain human approval

STATUS: PLANNING ONLY — NOT APPROVED

No video will be published automatically.
"""

with gr.Blocks(title="AI Video Factory") as demo:
    gr.Markdown("# AI Video Factory")
    gr.Markdown(
        "Stage 1 | Mobile Video Planning Dashboard"
    )

    topic = gr.Textbox(
        label="Video Topic",
        placeholder="e.g. Best Free AI Tools for Beginners"
    )
    audience = gr.Dropdown(
        ["USA", "Europe", "Worldwide"],
        value="USA",
        label="Target Audience"
    )
    duration = gr.Slider(
        6, 10, value=8, step=1,
        label="Video Duration (minutes)"
    )

    generate = gr.Button("Create Video Plan")
    output = gr.Markdown()

    generate.click(
        create_plan,
        inputs=[topic, audience, duration],
        outputs=output
    )

demo.launch(
    server_name="0.0.0.0",
    server_port=7860
)
