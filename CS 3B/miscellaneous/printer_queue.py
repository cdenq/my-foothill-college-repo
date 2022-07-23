'''
Random sample file made for fun. Not for "production".
'''

from collections import *

class PrinterStack:
    def __init__(self):
        self.stack = []
        return

    def enqueue(self, file):
        self.stack.append(f"{file}.jpg")
        print(f"{file}.jpg added.")
        return

    def dequeue(self):
        paper = self.stack.pop(0)
        print(f"Printed {paper}.")
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
    job = PrinterStack()
    print("Welcome to your office printer!")
    while True:
        ans = input("What would you like to do? Add job (1), print (2), "
                    "view history (3), or quit (4)?")
        if ans == "1":
            check = input("What file?")
            job.enqueue(check)
        elif ans == "2":
            if job.empty():
                print("empty!")
            else:
                job.dequeue()
        elif ans == "3":
            job.history()
        elif ans == "4":
            print("Exiting printer module. Thanks for using!")
            break
        else:
            print("Please pick a valid response.")

if __name__ == "__main__":
    main()