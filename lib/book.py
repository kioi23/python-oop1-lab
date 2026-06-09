#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        """Initialize a Book with a title and page count."""
        self.title = title
        self._page_count = None
        self.page_count = page_count
        self._current_page = 1
    
    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")
    
    def turn_page(self):
        """Turn to the next page."""
        if self._current_page < self.page_count:
            self._current_page += 1
            print("Flipping the page...wow, you read fast!")
        else:
            print("You've reached the end of the book!")
    
        