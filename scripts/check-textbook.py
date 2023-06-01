import sys
import os

textbook_size = os.stat("textbook.pdf").st_size
main_size = os.stat("main.pdf").st_size

print("textbook.pdf: ", textbook_size)
print("main.pdf: ", main_size)


diff_pct = abs(textbook_size - main_size) / textbook_size
print("diff_pct: ", diff_pct)
sys.exit(diff_pct > 0.02) 