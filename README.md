## Overview
This project is a [Wordle](https://www.nytimes.com/games/wordle/index.html) Helper that can help 
user see how many possible words there are and show what those words are. This can help Wordle 
players figure out their next play, and provide insights on how each of their plays reduce the 
possible number of words.

To run the program, type `python wordle_helper.py` or `python3 wordle_helper.py` in
the terminal. This program is written in `python3`.

**Note that the dictionary file used in this program is NOT the same one used for Wordle, so
there might be slight mismatch in what counts as valid words**


## Details
### The Dictionary File
The `dictionary_5_letters.txt` file used is a modified
version of `dictionary.txt` file (can be found from the University of Washington's
[CSE 143 Website](https://courses.cs.washington.edu/courses/cse143/22wi/homework/dictionary.txt)).

`dictionary_5_letters.txt` is created by `extract_words_by_length.py` with the input file of
`dictionary.txt` found above.

### Wordle Helper
The program is a command-line program which can output the possible words based on the user
words and the status of each letter (e.g. the letter is in the word but not in the dictionary).
It allows the user to replay the game multiple times.

### Example run of the program

The example run of this program use user plays based on [this tweet](https://twitter.com/NYTimesWordplay/status/1494053394419314689) by NYTimesWordPlay.
```
Number of possible words: 9330
Possible words (only show the first 50 words)
exits     spume     pixes     glout     slurs     wreak     hover     pares     alack     poise
duvet     surra     acing     menta     rusts     tarre     burro     balmy     wifey     cheat
odors     dinar     opens     redon     misos     flunk     raced     price     clach     lames
braza     cered     beses     boned     buddy     cubby     snell     upset     thews     flyer
bower     shale     limes     feebs     toric     holes     quote     oboli     cries     wecht

Enter the word you want to try: crane
Enter the information about above word in I, O, X format: XIIXX
Number of possible words: 335
Possible words (only show the first 50 words)
surra     targa     muras     hairs     tabor     yaird     thraw     zarfs     algor     parky
rakis     doura     taros     kafir     lairs     radii     harps     sapor     ratty     parka
raggs     tardy     horah     lazar     radix     rammy     rayah     ramus     foray     harpy
party     ratos     toras     sprag     boyar     rioja     bards     libra     moral     sards
auras     tarot     sprat     raggy     larum     tayra     padri     karma     varix     sugar

Enter the word you want to try: Barks
Enter the information about above word in I, O, X format: XIIXX
Number of possible words: 36
Possible words (only show the first 50 words)
algor     doura     rioja     jumar     filar     flora     pilar     alvar     agora     aport
polar     mudra     hijra     tolar     rugal     altar     augur     molar     riyal     lidar
aggro     gular     ixora     rhyta     volar     hydra     amort     ultra     amour     rival
ottar     moira     jowar     hilar     attar     royal

Enter the word you want to try: flora
Enter the information about above word in I, O, X format: XXOOO
User word: flora , curr word: agora
User word: flora , curr word: ixora
Number of possible words: 2
Possible words (only show the first 50 words)
agora     ixora

Enter the word you want to try: agora
Enter the information about above word in I, O, X format: OOOOO
Number of possible words: 1
Possible words (only show the first 50 words)
agora
```
