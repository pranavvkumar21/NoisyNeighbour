from moviepy import VideoFileClip, AudioFileClip
from pydub import AudioSegment
from pydub.effects import normalize
import os

def extract_audio_from_video(video_path):
    """Extracts audio from a video file and returns it as an AudioSegment."""
    video_path = str(video_path)
    video = VideoFileClip(video_path)
    audio_path = video_path.rsplit('.', 1)[0] + '.mp3'
    if not os.path.exists(audio_path):
        video.audio.write_audiofile(audio_path)
    else:
        print(f"Audio file already exists at: {audio_path}")
    return audio_path

def combine_audio_video(video_path, audio_path):
    """Combines a video file with a new audio file."""
    video_path = str(video_path)
    audio_path = str(audio_path)
    video = VideoFileClip(video_path)
    new_audio = AudioFileClip(audio_path)
    final_video = video.with_audio(new_audio)
    output_path = video_path.rsplit('.', 1)[0] + '_with_new_audio.mp4'
    final_video.write_videofile(output_path, codec='libx264', audio_codec='aac')
    return output_path

def sanitize_filename(filename):
    """Remove illegal filesystem characters"""
    # Replace illegal characters with underscores or remove them
    illegal_chars = r'[<>:"/\\|?*]'
    filename = re.sub(illegal_chars, '_', filename)  # or '' to remove
    filename = filename.strip()
    return filename



def preprocess_audio_for_demucs(audio_path, output_path):
    """Normalize audio before Demucs processing"""
    # Load audio
    audio = AudioSegment.from_file(audio_path)
    
    # Normalize to consistent volume
    normalized_audio = normalize(audio)
    
    # Export as high-quality WAV
    normalized_audio.export(
        output_path,
        format="wav",
        parameters=["-ar", "44100"]  # Standard sample rate
    )
    
    return output_path
