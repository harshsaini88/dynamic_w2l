import streamlit as st
import subprocess
import os
import tempfile

# Set up the Streamlit app
st.title("Lip-Sync Video Processing")

# File uploader for video and audio files
video_file = st.file_uploader("Upload Video", type=["mp4", "avi", "mov"])
audio_file = st.file_uploader("Upload Audio", type=["mp3", "wav"])

# Run the lip-sync process
if st.button("Process Video"):
    if video_file is not None and audio_file is not None:
        # Create a temporary directory for uploaded files
        with tempfile.TemporaryDirectory() as tempdir:
            # Save the uploaded files to the temporary directory
            video_path = os.path.join(tempdir, "uploaded_video" + os.path.splitext(video_file.name)[1])
            audio_path = os.path.join(tempdir, "uploaded_audio" + os.path.splitext(audio_file.name)[1])
            
            with open(video_path, "wb") as vfile:
                vfile.write(video_file.read())
            
            with open(audio_path, "wb") as afile:
                afile.write(audio_file.read())
            
            # Run the lip-sync command
            command = ["python", "run.py", "-video_file", video_path, "-vocal_file", audio_path]
            
            with st.spinner("Processing..."):
                result = subprocess.run(command, capture_output=True, text=True)
                if result.returncode == 0:
                    st.success("Processing completed successfully!")
                    st.video(video_path)  # Display the processed video
                else:
                    st.error("An error occurred during processing.")
                    st.text(result.stderr)  # Display error message
    else:
        st.error("Please upload both video and audio files.")
