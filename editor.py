from moviepy.editor import VideoFileClip, ColorClip, CompositeVideoClip
import os

def resize_video(input_path, output_path, target_width, target_height):
    # Load the video clip
    clip = VideoFileClip(input_path)
    
    # Calculate the aspect ratio of the original video
    aspect_ratio = clip.w / clip.h
    
    # Calculate new dimensions that maintain the aspect ratio
    if aspect_ratio > target_width / target_height:  # wider than tall
        new_width = target_width
        new_height = int(target_width / aspect_ratio)
    else:  # taller than wide
        new_height = target_height
        new_width = int(target_height * aspect_ratio)
    
    # Resize the clip while maintaining aspect ratio
    resized_clip = clip.resize(width=new_width, height=new_height)
    
    # Create a black background of the target size
    background = ColorClip(size=(target_width, target_height), color=(0,0,0))
    
    # Calculate the position to center the resized video
    x_offset = (target_width - new_width) // 2
    y_offset = (target_height - new_height) // 2
    
    # Create the final composite video
    final_clip = CompositeVideoClip([background, resized_clip.set_position((x_offset, y_offset))], 
                                    size=(target_width, target_height))
    final_clip = final_clip.set_duration(clip.duration)
    
    # Write the result to a file
    final_clip.write_videofile(output_path)
    
    # Close the clips to free up system resources
    clip.close()
    resized_clip.close()
    final_clip.close()
    
    # Delete the original file
    os.remove(input_path)