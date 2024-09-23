import tkinter as tk
from tkinter import filedialog
from MusicPlayer import DoublyLinkedList
import pygame
from PIL import Image, ImageTk
import os

class MusicPlayerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("600x400")  # Adjust window size as needed

        pygame.mixer.init()
        pygame.mixer.music.set_endevent(pygame.USEREVENT)  # Set an event to handle song end

        # Playlist management
        self.playlist = DoublyLinkedList()

        # Load button images
        self.play_img = ImageTk.PhotoImage(Image.open("play.png").resize((40, 40)))
        self.pause_img = ImageTk.PhotoImage(Image.open("play.png").resize((40, 40)))  # Corrected image for pause
        self.next_img = ImageTk.PhotoImage(Image.open("fast-forward.png").resize((40, 40)))
        self.previous_img = ImageTk.PhotoImage(Image.open("rewind-button.png").resize((40, 40)))
        self.display_img = ImageTk.PhotoImage(Image.open("display-frame.png").resize((30, 30)))  # Add display image
        self.add_img = ImageTk.PhotoImage(Image.open("add.png").resize((30, 30)))  # Add image
        self.delete_img = ImageTk.PhotoImage(Image.open("bin.png").resize((30, 30)))  # Delete image

        # Play/Pause toggle state
        self.is_paused = False
        self.info_box = None
        self.delete_box = None

        # Load GIF background image
        self.bg_img = ImageTk.PhotoImage(Image.open("music.jpg").resize((600, 400)))
        self.canvas = tk.Canvas(self.root, width=600, height=400)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_img)

        # Draw thicker white line at the bottom
        self.orange_line_color = "#FFFFFF"
        self.line_height = 50  # Increase height for the white line
        self.canvas.create_rectangle(0, 385 - self.line_height, 600, 400, fill=self.orange_line_color, outline=self.orange_line_color)

        # Frame for buttons to organize layout
        self.control_frame = tk.Frame(self.root, bg=self.orange_line_color)
        self.control_frame.place(relx=0.5, rely=1.0, anchor=tk.S)  # Center horizontally and place at bottom

        # Buttons - previous, play/pause, next, search
        self.previous_button = tk.Button(self.control_frame, image=self.previous_img, command=self.previous_music, bd=0, bg=self.orange_line_color)
        self.previous_button.grid(row=0, column=0, padx=10, pady=5)

        self.play_button = tk.Button(self.control_frame, image=self.play_img, command=self.play_pause_music, bd=0, bg=self.orange_line_color)
        self.play_button.grid(row=0, column=1, padx=10, pady=5)

        self.next_button = tk.Button(self.control_frame, image=self.next_img, command=self.next_music, bd=0, bg=self.orange_line_color)
        self.next_button.grid(row=0, column=2, padx=10, pady=5)


        # Playlist display
        self.playlist_box = tk.Listbox(self.root, bg="black", fg="white", width=50, height=10)
        self.playlist_box.pack(pady=10)
        self.update_playlist_display()

        # Top-right corner buttons
        self.top_right_frame = tk.Frame(self.root, bg=self.orange_line_color)
        self.top_right_frame.place(relx=1.0, rely=0.0, anchor=tk.NE)  # Place at top-right corner

        self.display_button = tk.Button(self.top_right_frame, image=self.display_img, command=self.display_playlist, bd=0, bg=self.orange_line_color)
        self.display_button.grid(row=0, column=0, padx=5, pady=5)

        self.add_button_top = tk.Button(self.top_right_frame, image=self.add_img, command=self.add_songs, bd=0, bg=self.orange_line_color)
        self.add_button_top.grid(row=1, column=0, padx=5, pady=5)

        self.delete_button = tk.Button(self.top_right_frame, image=self.delete_img, command=self.show_delete_box, bd=0, bg=self.orange_line_color)
        self.delete_button.grid(row=2, column=0, padx=5, pady=5)

        # Load initial songs
        self.load_initial_songs()

        # Start periodic check for music end
        self.check_music_end()
    def add_songs(self):
        files = filedialog.askopenfilenames(filetypes=[("Audio Files", "*.mp3")])
        for file in files:
            song_name = os.path.basename(file)  # Extract only the file name from the full path
            self.playlist.append(song_name)
            print(f"New song added: {song_name}")
        self.update_playlist_display()
        if not self.is_paused:
            self.play_pause_music()
    def load_initial_songs(self):
        # Add your song files here
        self.playlist.append("summer.mp3")
        self.playlist.append("night.mp3")
        self.playlist.append("travel.mp3")
        self.update_playlist_display()
        self.play_pause_music()  # Start playing the first song if songs are added

    def play_pause_music(self):
        try:
            if not self.is_paused:
                self.playlist.play_current()
                self.is_paused = True
                self.play_button.config(image=self.pause_img)  # Switch to pause button
            else:
                pygame.mixer.music.pause()
                self.is_paused = False
                self.play_button.config(image=self.play_img)  # Switch back to play button
        except pygame.error:
            print("Pygame error: ", pygame.get_error())

    def next_music(self):
        self.playlist.next()

    def previous_music(self):
        self.playlist.previous()

    def display_playlist(self):
        # Create the display box for the playlist
        self.info_box = tk.Toplevel(self.root)
        self.info_box.title("Playlist")
        self.info_box.geometry("350x350")
        self.info_box.configure(bg="#400090")  # Dark purple background
        self.info_box.transient(self.root)
        self.info_box.grab_set()
        self.info_box.focus_set()
        self.info_box.protocol("WM_DELETE_WINDOW", self.hide_info_box)

        # Title label
        tk.Label(self.info_box, text="Current Playlist", bg="#400090", fg="#FFFFFF", font=("Helvetica", 14, "bold")).pack(pady=10)

        # Playlist display listbox
        self.playlist_display = tk.Listbox(self.info_box, bg="#5e00d2", fg="#E0E0E0", selectbackground="#5A189A", width=40, height=15, bd=0)
        self.playlist_display.pack(pady=10)
        self.update_playlist_display_info_box()

    def update_playlist_display_info_box(self):
        self.playlist_display.delete(0, tk.END)  # Clear the listbox
        current = self.playlist.head
        while current:
            self.playlist_display.insert(tk.END, current.data)  # Insert song into listbox
            current = current.next

    def hide_info_box(self):
        if self.info_box:
            self.info_box.destroy()
            self.info_box = None

    def show_delete_box(self):
        self.delete_box = tk.Toplevel(self.root)
        self.delete_box.title("Delete Song")
        self.delete_box.geometry("350x200")
        self.delete_box.configure(bg="#6a1be4")  # Dark purple background
        self.delete_box.transient(self.root)
        self.delete_box.grab_set()
        self.delete_box.focus_set()
        self.delete_box.protocol("WM_DELETE_WINDOW", self.hide_delete_box)

        # Label for delete entry
        tk.Label(self.delete_box, text="Enter Song Name to Delete:", bg="#400090", fg="#FFFFFF", font=("Helvetica", 12, "bold")).pack(pady=15)

        # Entry field for song name
        self.delete_entry = tk.Entry(self.delete_box, width=40, bg="#5e00d2", fg="#FFFFFF", insertbackground="white")
        self.delete_entry.pack(pady=5)

        # Delete button
        self.delete_button = tk.Button(self.delete_box, text="Delete", command=self.delete_song, bg="#5A189A", fg="#FFFFFF", font=("Helvetica", 12, "bold"), bd=0, padx=10, pady=5)
        self.delete_button.pack(pady=10)

        # Bind click event
        self.delete_box.bind("<Button-1>", self.on_click_delete_box)

    def hide_delete_box(self):
        if self.delete_box:
            self.delete_box.destroy()
            self.delete_box = None

    def delete_song(self):
        song_name = self.delete_entry.get()
        self.playlist.delete(song_name)
        self.update_playlist_display()
        self.hide_delete_box()

    def check_music_end(self):
        """ Periodically check if the music has ended and handle it. """
        if not pygame.mixer.music.get_busy():  # If music is not playing
            self.playlist.handle_music_end()  # Handle the end of the song
        self.root.after(1000, self.check_music_end)  # Check every 1 second


    def update_playlist_display(self):
        self.playlist_box.delete(0, tk.END)  # Clear the listbox
        current = self.playlist.head
        while current:
            self.playlist_box.insert(tk.END, current.data)  # Insert song into listbox
            current = current.next

    def on_click_info_box(self, event):
        if self.info_box and not self.info_box.winfo_containing(event.x_root, event.y_root):
            self.hide_info_box()

    def on_click_search_box(self, event):
        if self.search_box and not self.search_box.winfo_containing(event.x_root, event.y_root):
            self.hide_search_box()

    def on_click_delete_box(self, event):
        if self.delete_box and not self.delete_box.winfo_containing(event.x_root, event.y_root):
            self.hide_delete_box()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayerGUI(root)
    root.mainloop()
