# starting pt (est. 30 min)
from now on, i'm kinda tired of typing formally. feel free to ask questions through discord if needed

overview:
- setting up vscode
- setting up python
- setting up pip
- setting up path

**note**: i enjoy coding on mac better. coding on your pc doesn't really give me motivation. if you don't have a laptop, feel free to stay on your pc

### vscode
download stable version of vscode for your operating system here: https://code.visualstudio.com/download
when downloading, there should be an option (maybe not) to add code to your PATH; check the box
after downloading, restart your computer and attempt to access a directory (folder) and open a terminal by:

(you should be in your root dir, where the name of your PC is shown)
vinh@hobin-i-ui-MacBook-Max-3 ~ % 

``cd`` = travel to a directory
``mkdir`` = create a directory
``code .`` = open vscode in this directory

terminal is case-sensitive, so make sure that you capitalize things efficiently

``cd Documents`` <-- you can do any flder, but i choose Documents for organization
``mkdir python-learning-src`` <-- making a folder for this lesson
``code .`` <-- opening VScode in this folder

if it successfully opened a VScode window, you've got it!

here's an early lesson on git: git is a version control program; meaning that you can "save" files, send it to a cloud up above, and on any device retrieve the same files that you originally pushed. meaning, you can work on any device without having to do any extra work.

git works through branches: you don't have to worry about this now.

start by installing git: https://git-scm.com/downloads ; and remember to add this to your PATH! this makes it able to be called in your regular terminal. no worries if there isn't an option.

``git`` is now a command in your terminal; good

if you haven't already made a github account, do so here: https://github.com/

once you do, head back to your terminal, travel to your folder that you made earlier in ``/Documents/python-learning-src``
and run ``git clone https://github.com/vznh/mentoring.git``. this will make a clone of the repository (project structure) that i have with me right now

while still in the same repository, ``git init`` and that will create an instance of git; essentially starting the version tracking of your repository

run these two commands while still in the same repo:
``git branch -M main``
``git remote add origin https://github.com/vznh/mentoring.git``

it will prompt for login credentials; do so.

from now on, everyday when you work, run ``git pull`` while in the same folder ``/Documents/python-learning-src`` to "pull" the latest version of my work for you.

you're all set!