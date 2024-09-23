import pygame

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.current = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                if current == self.current:
                    self.current = self.current.next or self.head
                return
            current = current.next

    def play_current(self):
        if self.current:
            pygame.mixer.music.load(self.current.data)
            pygame.mixer.music.play()

    def next(self):
        if self.current and self.current.next:
            self.current = self.current.next
            self.play_current()
        else:
            self.stop_music()
            print("No more songs in playlist.")

    def previous(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            self.play_current()
        else:
            self.stop_music()
            print("No previous song available.")

    def pause(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def handle_music_end(self):
        if self.current and self.current.next:
            self.current = self.current.next
            self.play_current()
        else:
            self.stop_music()
            print("No more songs in playlist.")
