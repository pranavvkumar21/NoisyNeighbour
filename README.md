NoisyNeighbour
AI-Powered Karaoke Generator from YouTube Videos

NoisyNeighbour downloads videos from YouTube, uses AI to separate vocals from instrumentals, and creates custom karaoke tracks. Perfect for music enthusiasts, content creators, and karaoke lovers!

✨ Features
🎵 Smart Downloading - Download full video or audio-only from YouTube

🎼 AI Vocal Separation - Powered by Meta's Demucs to split vocals and instrumentals

🎥 Karaoke Video Creation - Automatically combines instrumental track with original video

📁 Organized Output - Auto-creates folders with thumbnails and proper file structure

⚡ Flexible Workflow - Works with both video and audio-only modes

🔄 Efficient Processing - Caches downloads to avoid re-processing

Will add a dashboard in the future and cpu support

Quick Start
Installation
bash
# Clone the repository
```
git clone https://github.com/yourusername/NoisyNeighbour.git
cd NoisyNeighbour
```
# Install Python dependencies
```
pip install -r requirements.txt
```

# Install FFmpeg (required for audio/video processing)
```
# Ubuntu/Debian:
sudo apt-get install ffmpeg

# macOS:
brew install ffmpeg

# Or via conda:
conda install -c conda-forge ffmpeg
```

# Basic Usage
Create a karaoke video from YouTube:
```
python main.py --url "https://www.youtube.com/watch?v=VIDEO_ID"
```

Download audio only and split into stems:
```
python main.py --url "https://www.youtube.com/watch?v=VIDEO_ID" --audio_only
```

Custom download location:
```
python main.py --url "https://www.youtube.com/watch?v=VIDEO_ID" 
    --download_path "./my_music"
```

📖 Command Line Options
```
usage: main.py [-h] [--url URL] [--download_path DOWNLOAD_PATH] [--audio_only]

options:
  -h, --help            Show this help message and exit
  --url URL             The URL of the YouTube video to process
  --download_path PATH  Path to download files (default: ./data)
  --audio_only          Download audio only, skip video processing
```