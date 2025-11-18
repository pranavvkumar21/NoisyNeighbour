from moviepy import VideoFileClip, AudioFileClip, ImageClip, concatenate_videoclips

def create_lyric_synced_video(
    video_path,
    audio_path,
    frame_audio_intervals,
    output_path="output.mp4"
):
    """
    Create video with specific frames shown at specific audio time intervals.

    Args:
        video_path (str): Path to the source video
        audio_path (str): Path to high quality audio
        frame_audio_intervals (list of tuples):
            [(frame_time, audio_start, audio_end), ...]
            frame_time: timestamp in video to grab frame from (sec)
            audio_start, audio_end: start and end time in audio to display that frame (sec)
        output_path (str): Path to save output video

    Returns:
        str: output video path
    """
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)

    clips = []

    for frame_time, audio_start, audio_end in frame_audio_intervals:
        duration = audio_end - audio_start
        # Get frame at frame_time (numpy array)
        frame = video.get_frame(frame_time)

        # Create ImageClip of frame with duration
        img_clip = ImageClip(frame).with_duration(duration)
        img_clip = img_clip.with_fps(video.fps).resized(video.size)
        
        # Set start time of clip to audio_start to align with audio timeline
        img_clip = img_clip.with_start(audio_start)
        
        clips.append(img_clip)

    # Compose all clips on timeline (duration = audio duration)
    final_video = concatenate_videoclips(clips, method='compose')
    
    # Set audio track (high quality)
    final_video = final_video.with_audio(audio)
    
    # Set full duration to audio duration
    final_video = final_video.with_duration(audio.duration)

    # Export final video
    final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")

    # Clean up
    video.close()
    audio.close()
    final_video.close()

    return output_path


if __name__ == "__main__":
    video_file = "/home/pranav/NoisyNeighbour/scriptsd/ശരണമയ്യപ്പാ സ്വാമി ｜ Saranamayyappa ｜ Song with Lyrics｜ Ayyappa Bhajana.mp4"
    audio_file = "/home/pranav/NoisyNeighbour/scriptsd/ശരണമയ്യപ്പാ സ്വാമി ശരണമയ്യപ്പാ ｜ Ayyappa Songs 2020 ｜ Saranamayyappa Swami Song_normalized_instrumental.wav"
    
    # Define list of (frame_time_in_video, audio_start_time, audio_end_time)
    timings = [
        (5, 0, 43),       # Show frame at 5s in video from 0 to 43 sec of audio
        (40, 43, 2*60 +18),      # Show frame at 40s in video from 43 to 138 sec of audio
        (1*60 + 40, 2*60 + 18, 3*60+55), 
        (2*60 + 40, 3*60+55, 4*60+48),
        (3*60 + 30, 4*60+48, 5*60+49)    # Show frame at 20s in video from 9 to 15 sec of audio
        # Add more as needed
    ]
    
    output_path = "lyric_sync_output.mp4"
    path = create_lyric_synced_video(video_file, audio_file, timings, output_path)
    print(f"Video saved to {path}")
