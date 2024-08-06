import tkinter as tk
from tkinter import filedialog
import pygame

def load_song():
    """Load a song for playback."""
    filepath = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
    if filepath:
        pygame.mixer.music.load(filepath)
        label_song.config(text=f"Loaded: {filepath.split('/')[-1]}")

def play_song():
    """Play the loaded song."""
    pygame.mixer.music.play()

def pause_song():
    """Pause the song."""
    pygame.mixer.music.pause()

def resume_song():
    """Resume the song."""
    pygame.mixer.music.unpause()

def stop_song():
    """Stop the song."""
    pygame.mixer.music.stop()

# Initialize pygame mixer
pygame.mixer.init()

# Create the main window
root = tk.Tk()
root.title("Simple Music Player")

# Create and place widgets
button_load = tk.Button(root, text="Load Song", command=load_song)
button_load.pack()

button_play = tk.Button(root, text="Play", command=play_song)
button_play.pack()

button_pause = tk.Button(root, text="Pause", command=pause_song)
button_pause.pack()

button_resume = tk.Button(root, text="Resume", command=resume_song)
button_resume.pack()

button_stop = tk.Button(root, text="Stop", command=stop_song)
button_stop.pack()

label_song = tk.Label(root, text="No song loaded")
label_song.pack()

# Start the main loop
root.mainloop()
import tkinter as tk
from tkinter import filedialog
import pygame

def load_song():
    """Load a song for playback."""
    filepath = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
    if filepath:
        pygame.mixer.music.load(filepath)
        label_song.config(text=f"Loaded: {filepath.split('/')[-1]}")

def play_song():
    """Play the loaded song."""
    pygame.mixer.music.play()

def pause_song():
    """Pause the song."""
    pygame.mixer.music.pause()

def resume_song():
    """Resume the song."""
    pygame.mixer.music.unpause()

def stop_song():
    """Stop the song."""
    pygame.mixer.music.stop()

# Initialize pygame mixer
pygame.mixer.init()

# Create the main window
root = tk.Tk()
root.title("Simple Music Player")

# Create and place widgets
button_load = tk.Button(root, text="Load Song", command=load_song)
button_load.pack()

button_play = tk.Button(root, text="Play", command=play_song)
button_play.pack()

button_pause = tk.Button(root, text="Pause", command=pause_song)
button_pause.pack()

button_resume = tk.Button(root, text="Resume", command=resume_song)
button_resume.pack()

button_stop = tk.Button(root, text="Stop", command=stop_song)
button_stop.pack()

label_song = tk.Label(root, text="No song loaded")
label_song.pack()

# Start the main loop
root.mainloop()
