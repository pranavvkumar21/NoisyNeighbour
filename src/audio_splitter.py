#!/usr/bin/env python3
import os
import shutil
import torchaudio
from demucs.apply import apply_model
from demucs.pretrained import get_model
from demucs.audio import convert_audio
import soundfile as sf


class AudioSplitter:
    def __init__(self):
        self.model = get_model(name="htdemucs")
    def split_audio(self, audio_path):
        # Load the audio file
        print(f"Loading audio file: {audio_path}")
        wav, sr = torchaudio.load(audio_path)
        wav = convert_audio(wav, sr, self.model.samplerate, self.model.audio_channels)

        # Apply the model to separate the sources
        print("separating sources...")
        sources = apply_model(self.model, wav[None])[0]
        stem_names = self.model.sources
        # get instrumental
        inst = sum([s for i, s in enumerate(sources) if stem_names[i] != "vocals"])
        vocals = sources[stem_names.index("vocals")]
        # Save the instrumental version
        print("Saving instrumental version...")
        instrumental_path = os.path.splitext(audio_path)[0] + "_instrumental.wav"
        sf.write(instrumental_path, inst.T.numpy(), self.model.samplerate)
        #save the vocal version
        print("Saving vocal version...")
        vocal_path = os.path.splitext(audio_path)[0] + "_vocals.wav"
        sf.write(vocal_path, vocals.T.numpy(), self.model.samplerate)
        print(f"Instrumental saved to: {instrumental_path}")
        print(f"Vocals saved to: {vocal_path}")
        return instrumental_path, vocal_path

if __name__ == "__main__":
    audio_splitter = AudioSplitter()
    audio_splitter.split_audio("")
    print("Audio split successfully.")