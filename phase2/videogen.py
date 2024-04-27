from moviepy.editor import TextClip, ImageClip, concatenate_videoclips

# Define the conversation and emojis
conversation = [
    ("😀", "Hello, how are you?"),
    ("🤖", "I'm good, thanks for asking!"),
    ("😀", "What are you doing today?"),
    ("🤖", "Just chatting with you.")
]

# Path to emoji images
emoji_paths = {
    "😀": "./phase2/smiling_imp.png",  # Update with actual paths
    "🤖": "./phase2/robot_face.png"
}

# Generate clips
clips = []
for emoji, text in conversation:
    # Create an image clip with the emoji
    img_clip = ImageClip(emoji_paths[emoji], duration=2)
    
    # Create a text clip
    txt_clip = TextClip(text, fontsize=24, color='white', bg_color='black', size=img_clip.size).set_duration(2)
    
    # Overlay text on image
    video = ImageClip(emoji_paths[emoji], duration=2).set_opacity(0).set_position("center").set_duration(2)
    final_clip = CompositeVideoClip([img_clip, txt_clip.set_pos("bottom")])
    
    clips.append(final_clip)

# Concatenate clips
final_video = concatenate_videoclips(clips)

# Write the result to a file
final_video.write_videofile("emoji_conversation.mp4", codec="libx264", fps=24)
