import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import soundfile as sf
from scipy.signal import butter, filtfilt

# Generate test audio file
def generate_test_audio(filename, duration=5, sr=44100):
    """
    Generate a test audio file with a combination of sine wave frequencies and noise.
    :param filename: output file name
    :param duration: duration of the audio file (seconds)
    :param sr: sampling rate
    """
    t = np.linspace(0, duration, int(sr * duration), endpoint=False)
    
    # Sine wave signals with different frequencies
    freq1 = 440  # First frequency: 440 Hz (A note)
    freq2 = 880  # Second frequency: 880 Hz
    clean_signal = 0.5 * np.sin(2 * np.pi * freq1 * t) + 0.5 * np.sin(2 * np.pi * freq2 * t)
    
    # White noise
    noise = 0.2 * np.random.normal(0, 1, len(t))
    
    # Final signal: clean signal + noise
    noisy_signal = clean_signal + noise
    
    # Save the signal as an audio file
    sf.write(filename, noisy_signal, sr)
    print(f"Test audio file generated: {filename}")

# Function to design a low-pass filter
def butter_lowpass(cutoff, fs, order=4):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

# Apply the low-pass filter
def apply_filter(data, cutoff, fs, order=4):
    b, a = butter_lowpass(cutoff, fs, order)
    return filtfilt(b, a, data)

# Start process
audio_file = "noisy_audio.wav"
generate_test_audio(audio_file)

# Read the generated audio file
signal, sr = librosa.load(audio_file, sr=None)

# Frequency spectrum analysis
fft_signal = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(fft_signal), 1/sr)

# Identify noise and determine cutoff frequency
threshold = np.mean(np.abs(fft_signal)) * 2
noise_freqs = frequencies[np.abs(fft_signal) > threshold]
cutoff = max(np.abs(noise_freqs)) if len(noise_freqs) > 0 else sr // 2
print(f"Noise detected. Cutoff frequency: {cutoff:.2f} Hz")

# Manually adjust cutoff frequency
cutoff = 1000  # Manually set cutoff frequency to remove more noise
print(f"Using cutoff frequency: {cutoff} Hz")

# Filter the signal
filtered_signal = apply_filter(signal, cutoff, sr, order=6)  # Increase filter order to 6

# Save the cleaned signal
output_file = "clean_audio.wav"
sf.write(output_file, filtered_signal, sr)
print(f"Cleaned audio file saved: {output_file}")

# Plot the graphs
plt.figure(figsize=(12, 8))

# Noisy signal
plt.subplot(3, 1, 1)
librosa.display.waveshow(signal, sr=sr, alpha=0.75)
plt.title("Noisy Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")

# Frequency spectrum of the noisy signal
plt.subplot(3, 1, 2)
plt.stem(frequencies[:len(frequencies)//2], np.abs(fft_signal)[:len(frequencies)//2])  # Removed use_line_collection=True
plt.title("Frequency Spectrum of Noisy Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")

# Signal after noise removal
plt.subplot(3, 1, 3)
librosa.display.waveshow(filtered_signal, sr=sr, alpha=0.75, color="orange")
plt.title("Signal After Noise Removal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()





