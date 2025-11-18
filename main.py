import os
import argparse

from src.audio_downloader import AudioDownloader
from src.audio_splitter import AudioSplitter
from src.processing import extract_audio_from_video, combine_audio_video, preprocess_audio_for_demucs

from pathlib import Path

parser = argparse.ArgumentParser(description="Download, split, and process audio from a video URL.")
parser.add_argument("--url", type=str, help="The URL of the video to download audio from.")
parser.add_argument("--download_path", type=str, default="./data", help="Path to download the audio and video files.")
parser.add_argument("--audio-only", action="store_true", default=False, help="Download audio only if set; otherwise download full video.")

def main():
    args = parser.parse_args()
    url = args.url
    download_path = args.download_path
    audio_only = args.audio_only

    # Step 1: Download audio or video
    print("Step 1: Starting download...")
    downloader = AudioDownloader(download_path=download_path, audio_only=audio_only)
    media_path = downloader.download_audio(url)
    media_path = Path(media_path)
    print(f"\tDownloaded media to: {media_path}")

    # Step 2: If full video was downloaded, extract audio
    if not audio_only:
        print("Step 2: Extracting audio from video...")
        extracted_audio_path = extract_audio_from_video(media_path)
        print(f"\tExtracted audio to: {extracted_audio_path}")
    else:
        extracted_audio_path = media_path

    # Step 2.5: Preprocess audio for Demucs
    print("Step 2.5: Preprocessing audio for Demucs...")
    normalized_audio_path = str(extracted_audio_path).rsplit('.', 1)[0] + "_normalized.wav"
    extracted_audio_path = preprocess_audio_for_demucs(extracted_audio_path, normalized_audio_path)
    print(f"\tPreprocessed audio saved to: {extracted_audio_path}")

    # Step 3: Split the audio into vocals and instrumental
    print("Step 3: Splitting audio into vocals and instrumental...")
    audio_splitter = AudioSplitter()
    instrumental_path, vocal_path = audio_splitter.split_audio(extracted_audio_path)
    print(f"\tInstrumental audio saved to: {instrumental_path}")
    print(f"\tVocal audio saved to: {vocal_path}")
    # Step 4: Combine the original video with the instrumental audio
    if not audio_only:
        print("Step 4: Combining video with instrumental audio...")
        final_video_path = combine_audio_video(media_path, instrumental_path)
        print(f"\tFinal video with instrumental audio saved to: {final_video_path}")
    else:
        print(f"\tInstrumental audio saved to: {instrumental_path}")
        print(f"\tVocal audio saved to: {vocal_path}")

if __name__ == "__main__":
    main()
        
    
