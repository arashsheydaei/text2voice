import tkinter as tk
import subprocess

class TextToSpeechApp:
    def __init__(self, master):
        self.master = master
        self.master.title("text 2 voice")
        self.master.geometry("400x300")

        self.label = tk.Label(master, text="Enter ur text:")
        self.label.pack(pady=10)

        self.text_entry = tk.Entry(master, width=50)
        self.text_entry.pack(pady=10)

        self.convert_button = tk.Button(master, text="convert to voice", command=self.convert_to_speech)
        self.convert_button.pack(pady=10)

        self.voice_speed_label = tk.Label(master, text="speed change")
        self.voice_speed_label.pack(pady=5)
        self.voice_speed = tk.Scale(master, from_=80, to=450, orient='horizontal')
        self.voice_speed.set(175)  # سرعت پیش‌فرض
        self.voice_speed.pack(pady=5)

        self.voice_pitch_label = tk.Label(master, text="Pitch adjustment:")
        self.voice_pitch_label.pack(pady=5)
        self.voice_pitch = tk.Scale(master, from_=0, to=100, orient='horizontal')
        self.voice_pitch.set(50)  # زیر و بمی پیش‌فرض
        self.voice_pitch.pack(pady=5)

    def convert_to_speech(self):
        text = self.text_entry.get()
        if text:
            try:
                speed = self.voice_speed.get()
                pitch = self.voice_pitch.get()
                # استفاده از espeak برای تبدیل متن به گفتار با تنظیمات صدا
                subprocess.run(['espeak', '-v', 'fa', '-s', str(speed), '-p', str(pitch), text])
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()
