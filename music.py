import pygame
import os

class Node:
    def __init__(self, file_path=None):
        self.file_path = file_path
        self.song_name = os.path.basename(file_path) if file_path else None
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def append(self, file_path):
        new_node = Node(file_path)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.current = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete(self, song_name):
        temp = self.head
        while temp is not None:
            if temp.song_name == song_name:
                if temp == self.head and temp == self.tail:
                    self.head = None
                    self.tail = None
                    self.current = None
                elif temp == self.head:
                    self.head = self.head.next
                    self.head.prev = None
                elif temp == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev

                if self.current == temp:
                    self.current = self.head  # Reset to the head after deletion
                print(f"Deleted {song_name}")
                return
            temp = temp.next
        print(f"Song {song_name} not found in the playlist.")

    def play_current(self):
        if self.current:
            try:
                pygame.mixer.music.load(self.current.file_path)
                pygame.mixer.music.play()
                print(f"Now playing: {self.current.song_name}")
            except pygame.error:
                print("Error playing the file. Please make sure the file is an MP3 and exists.")
        else:
            print("No songs to play.")

    def next(self):
        if self.current and self.current.next:
            self.current = self.current.next
            self.play_current()
        else:
            print("No more songs in the playlist.")

    def previous(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            self.play_current()
        else:
            print("No previous song available.")

    def display_playlist(self):
        temp = self.head
        if temp is None:
            print("Playlist is empty.")
            return
        print("Playlist:")
        while temp is not None:
            current_marker = " <-- Current" if temp == self.current else ""
            print(f"- {temp.song_name}{current_marker}")
            temp = temp.next


# Main program logic
def menu():
    pygame.mixer.init()  # Initialize pygame mixer for playing audio
    playlist = DoublyLinkedList()

    while True:
        print("\n--- Music Player Menu ---")
        print("1. Add Song")
        print("2. Play Current Song")
        print("3. Play Next Song")
        print("4. Play Previous Song")
        print("5. Delete Song")
        print("6. Display Playlist")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            song_path = input("Enter the full path of the song (MP3 file): ")
            if os.path.exists(song_path) and song_path.endswith('.mp3'):
                playlist.append(song_path)
                print(f"{os.path.basename(song_path)} added to playlist.")
            else:
                print("Invalid file path or format. Please provide a valid MP3 file.")
        elif choice == "2":
            playlist.play_current()
        elif choice == "3":
            playlist.next()
        elif choice == "4":
            playlist.previous()
        elif choice == "5":
            song_name = input("Enter the song name to delete: ")
            playlist.delete(song_name)
        elif choice == "6":
            playlist.display_playlist()
        elif choice == "7":
            print("Exiting music player...")
            pygame.mixer.music.stop()  # Stop any playing music
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 8.")

if __name__ == "__main__":
    menu()
