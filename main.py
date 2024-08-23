from editor import resize_video
from downloader import download_video
print("AAAAAAAAAAAAAAAAAAAA")


video = input("Enter the URL of the Instagram Reel: ")

download_video(video)
input_video = "instagram-vids/video.mp4"
output_video = "final_vids/resized_video_1080x1920.mp4"
target_width = 1080
target_height = 1920

resize_video(input_video, output_video, target_width, target_height)

