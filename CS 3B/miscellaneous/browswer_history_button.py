'''
Random sample file made for fun. Not for "production".
'''

from collections import *

class BrowserStack:
    def __init__(self):
        self.stack = []
        return

    def visit(self, url):
        self.stack.append(f"www.{url}.com")
        print(f"www.{url}.com loaded.")
        return

    def back(self):
        if len(self.stack) >= 2:
            print(f"Left {self.stack[-1]}, now loaded {self.stack[-2]}.")
        else:
            print(f"Left {self.stack[-1]}. Now empty home page.")
        self.stack.pop()
        return

    def history(self):
        print("Here is your history:")
        if self.empty():
            print("empty")
        else:
            for i in self.stack:
                print(i)
        return

    def empty(self):
        if not self.stack:
            return True

def main():
    page = BrowserStack()
    done = False
    print("Welcome to Google.com!")
    while True:
        ans = input("What would you like to do? Visit URL (1), back (2), "
                    "view history (3), or quit (4)?")
        if ans == "1":
            check = input("Which site?")
            page.visit(check)
        elif ans == "2":
            if page.empty():
                print("No history for this page.")
            else:
                page.back()
        elif ans == "3":
            page.history()
        elif ans == "4":
            print("Exiting browser. Thanks for using!")
            break
        else:
            print("Please pick a valid response.")

if __name__ == "__main__":
    main()