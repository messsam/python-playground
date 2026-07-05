from pathlib import Path # Could word with both absolute and relative paths.

path1 = Path() # Automatically references the current directory.
path2 = Path('ecommerce')
# print(path2.exists())
emails_path = Path('emails')
if emails_path.exists():
    emails_path.rmdir()
emails_path.mkdir()
# print(emails_path.exists())

for file in Path('util').glob('*'):
    print(file)