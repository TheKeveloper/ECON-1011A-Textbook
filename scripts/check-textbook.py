import sys
import os

textbook_size = os.stat("textbook.pdf").st_size
main_size = os.stat("main.pdf").st_size

print("textbook.pdf:", textbook_size)
print("main.pdf:", main_size)

sys.exit(textbook_size != main_size) 