import gradio as gr
import subprocess
import os

# Function to handle lip-sync processing
def lip_sync(video_file, audio_file):
    if video_file is None or audio_file is None:
        return "Please upload both video and audio files.", None

    # Save the uploaded files
    video_path = "uploaded_video" + os.path.splitext(video_file.name)[1]
    audio_path = "uploaded_audio" + os.path.splitext(audio_file.name)[1]
    
    with open(video_path, "wb") as vfile:
        vfile.write(video_file.read())
    
    with open(audio_path, "wb") as afile:
        afile.write(audio_file.read())
    
    # Run the lip-sync command
    command = ["python", "run.py", "-video_file", video_path, "-vocal_file", audio_path]
    
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.returncode == 0:
        return "Processing completed successfully!", video_path  # Return video path to display
    else:
        return f"An error occurred: {result.stderr}", None

# Create the Gradio interface
interface = gr.Interface(
    fn=lip_sync,
    inputs=[
        gr.inputs.File(label="Upload Video", type="file", file_types=[".mp4", ".avi", ".mov"]),
        gr.inputs.File(label="Upload Audio", type="file", file_types=[".mp3", ".wav"])
    ],
    outputs=[
        gr.outputs.Textbox(label="Status"),
        gr.outputs.Video(label="Processed Video")
    ],
    title="Lip-Sync Video Processing",
    description="Upload a video and an audio file to lip-sync the video with the audio."
)

# Launch the Gradio app
interface.launch()
