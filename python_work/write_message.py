from pathlib import Path
path = Path('message.txt')
contents = 'Holy cow \n'
contents += 'lets go! \n'
contents += 'yes!!!! \n'
path.write_text(contents)
