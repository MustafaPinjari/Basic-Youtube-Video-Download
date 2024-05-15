from pytube import YouTube

link = input("Enter the YouTube video URL: ")
# link = "https://youtu.be/jQuEKLiEANs?si=4suzv1p_aXyF_OWR"

try:
    # Create a YouTube object
    yt = YouTube(link)

    # Select the first stream (usually the highest quality)
    video_stream = yt.streams.first()

    # Specify the directory where you want to save the downloaded video
    output_path = 'C:\\Users\\mustafa\\Downloads'  # Use forward slashes or double backslashes

    # Download the video to the specified directory
    video_stream.download(output_path=output_path)

    print(f'Download: {yt.title}')
except Exception as e:
    print(f"An error occurred: {str(e)}")
