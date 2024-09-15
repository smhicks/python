from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print('file not found!!!')
else:
    words = contents.split()
    num_words = len(words)
    print(f"the file {path} has {num_words} words. ")