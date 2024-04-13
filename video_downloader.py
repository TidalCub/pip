from pytube import YouTube

def download_video(url, output_path):
  try:
    # Create a YouTube object
    video = YouTube(url)

    # Get the highest resolution stream
    stream = video.streams.get_highest_resolution()

    # Download the video
    stream.download(output_path)

    print("Video downloaded successfully!")
  except Exception as e:
    print("Error:", str(e))

# Example usage
video_url = "https://www.youtube.com/watch?v=BcOIKdMfAQE"
output_folder = "./"
download_video(video_url, output_folder)