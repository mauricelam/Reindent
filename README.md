Reindent (Sublime Text 2 plugin)
==========

Reindent is a collection of functionalities related to reindentation. 
1. Paste and Reindent (Cmd + Shift + V / Ctrl + Shift + V) reindents the pasted text, which indents line pasting as well as multiline pasting. 
2. Move up / down and Reindent (Cmd + Ctrl + up / Ctrl + Shift + up) swaps the current line up or down, and then reindents them. The reindentation built-in to Sublime is a bit flaky on indentation based languages, so by default it is turned off in Python. To add / remove languages from the black list, modify `exclude_language_from_move` array in the settings.


Installation
----------

Download all the files in this repository and place it in your Sublime packages folder. 
* On the Mac it is `~/Library/Application Support/Sublime Text 2/Packages/Reindent`
