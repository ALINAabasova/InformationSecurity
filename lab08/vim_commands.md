# Vim commands explored (Lab 8 task)

## Modes
- i        enter INSERT mode (type text)
- Esc      back to NORMAL mode
- v        VISUAL mode (select text)
- :        COMMAND mode

## Moving around (normal mode)
- h j k l  left, down, up, right
- w / b    next / previous word
- 0 / $    start / end of line
- gg / G   first / last line
- :n       jump to line n

## Editing
- dd       delete current line
- 3dd      delete 3 lines
- yy       copy (yank) line
- p        paste
- u        undo
- Ctrl+r   redo
- x        delete one character
- r        replace one character

## Search and replace
- /word          search forward for "word"
- n / N          next / previous match
- :%s/old/new/g  replace all "old" with "new" in file

## Saving and quitting
- :w       save
- :q       quit
- :wq      save and quit
- :q!      quit without saving
- :%d      delete all content
