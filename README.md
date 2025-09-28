# Signal Denoising with Low-Pass Butterworth Filter and FFT Analysis (DSP Project)

This project explores the fundamental techniques of Digital Signal Processing (DSP) for **signal denoising**. It demonstrates the process of generating a noisy composite signal, analyzing its frequency components using the **Fast Fourier Transform (FFT)**, and effectively removing high-frequency noise using a designed **Low-Pass Butterworth Filter**.

## 💡 Project Goal & Methodology

The primary objective is to restore a clean signal embedded within White Noise by applying frequency-domain analysis and filtering.

### Methodology Pipeline:

1.  **Signal Generation:** Create a composite base signal from two distinct low-frequency sinusoids (representing clean data/audio).
2.  **Noise Injection:** Introduce **Gaussian White Noise** to the clean signal to simulate real-world data corruption.
3.  **Frequency Analysis (FFT):** Use the Fast Fourier Transform to convert the noisy signal from the time domain to the frequency domain, allowing clear identification of the high-frequency noise components.
4.  **Filter Design:** Design a high-order **Low-Pass Butterworth Filter** with a precise cutoff frequency determined by the spectral analysis.
5.  **Denoising:** Apply the filter to the noisy signal to attenuate frequencies above the cutoff, resulting in a significantly cleaner signal.

## ⚙️ Key Concepts Demonstrated

| Concept | Technique/File | Application |
| :--- | :--- | :--- |
| **Spectral Analysis** | `numpy.fft.fft` and `fftfreq` | Identifying the frequency signature of the base signal and the noise. |
| **Filtering** | `scipy.signal.butter` | Designing the recursive Butterworth filter for a flat passband. |
| **Noise Model** | `numpy.random.normal` | Generation and characteristics of **White Noise** (constant power across all frequencies). |
| **Signal Generation** | `mathmeta.py` | Creation of the base clean signal from discrete sinusoidal waves. |

## 📁 Repository Structure

| File Name | Purpose |
| :--- | :--- |
| `mathmeta.py` | The core Python script containing the entire DSP pipeline: signal generation, noise injection, FFT analysis, filter design, and denoising logic. |
| `clean_audio.wav` | Output file for the original, clean signal (generated for demonstration). |
| `noisy_audio.wav` | Output file for the signal after the White Noise has been injected. |
| `README.txt` | Original project documentation (contains detailed explanation of White Noise). |
| *Plots* | Expected to contain visualizations of the signal (Time Domain vs. Frequency Domain) before and after filtering. |

## 🚀 Getting Started

### 1. Prerequisites

This project relies on Python's scientific computing stack.

```bash
pip install numpy scipy matplotlib
```

### 2.Execution

To run the complete DSP process and generate the output files and visualizations, execute the main logic script:

```bash
python mathmeta.py
```
