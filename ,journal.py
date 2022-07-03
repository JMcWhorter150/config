import os, sys, tempfile

from datetime import datetime, timedelta
from pathlib import Path
from subprocess import call
# first need to create year, month, and day variables for yesterday
date = datetime.now() - timedelta(days=1)
year = str(date.year)
month = str(date.month)
day = str(date.day)

# specify the editor command
EDITOR = os.environ.get('EDITOR', 'nvim')
Path(f'/home/jmcwho/journal/{year}/{month}/').mkdir(parents=True, exist_ok=True)
location = f'/home/jmcwho/journal/{year}/{month}/'
file_name = f'{year}_{month}_{day}.md'
current_location = os.getcwd()
with open(location + file_name, 'w') as f:
    os.chdir(location)
    call([EDITOR, f.name])
    os.chdir(current_location)
