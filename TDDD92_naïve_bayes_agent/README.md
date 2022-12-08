# StarCraft II Python Bot
This repository contains a passive PyCommandCenter-based bot for StarCraft II. It is intended to be a reasonable starting point for creating your own StarCraft II-playing system.

## Setup for creating your own bot

1. You need to have your own fork ("copy") of this project and its repository. If you are participating in TDDD92, **you should *not* create your own fork!**  Instead, begin by registering your group in Webreg.  We periodically run a script that forks this project for all registered groups, placing projects in the [TDDD92-2021 group](https://gitlab.liu.se/tddd92-2021).  We will require you to use these projects and repositories.

2. Now clone the repository from Gitlab using the following command: `git clone <path>`, where `<path>` is shown when you press the blue button *Clone* in the top-right corner on your repository page. If you have configured SSH-access, then use the SSH link, otherwise use the HTTP link.

3. Next, set up the library in PyCharm. See [PyCommandCenter's page on PyCharm](https://gitlab.liu.se/starcraft-ai-course/pycommandcenter/blob/master/pycharm.md) for instructions.

4. Everything is now ready for PyCharm: Start PyCharm, and then select "Open" and navigate to the location you cloned your fork of this repository to.

5. In order to run the code, right click the file named "start.py" in the
   project panel to the right, and select "Debug main". This will run the code
   in "start.py", and consequently start StarCraft II. You can also edit the
   code in "start.py" by double-clicking "start.py".

6. Rename the folder 'myagent' to something unique, preferably with your group number
   in the name. This will make it easier when you want to run against other bots. So make
   sure ALL of the source code for the bot lives in that folder.

## Additional functionality

The *visualdebugger* folder contains a starting point for creating visual debug tools for various AI-related functionalties.  This may or may not be of use to you.  For TDDD92 specifically, this will be more useful in the second period when you begin to implement a selected AI technique.

The file `tictoc.py` may be useful for timing various parts of an agent. This is also more useful in the second half of TDDD92.
