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
proms     foist     kafir     plead     sente     apsis     glyph     heres     spook     jacks
fakir     lists     crake     sagas     cimex     forte     sunup     chins     hansa     kanji
fovea     alias     tutty     faced     yoked     geums     unpeg     anion     homer     torrs
fists     jorum     sweep     bears     trows     prose     genus     profs     hirer     clegs
pitot     erses     germy     guess     enjoy     cosey     wakes     fugio     turrs     dinks

Enter the word you want to try: crane
Enter the information about above word in I, O, X format: XIIXX
Number of possible words: 335
Possible words (only show the first 50 words)
kafir     fakir     talar     rafts     mayor     makar     harps     libra     pargo     stray
doura     parks     afrit     larks     strap     wairs     tarry     joram     yards     raids
ragis     larky     aargh     rails     foray     sprag     burka     rakus     rasps     taros
barfi     varas     purda     asura     varus     karoo     moray     altar     harms     agora
abris     vairs     hilar     parts     barbs     faqir     supra     harpy     sabir     riyal

Enter the word you want to try: barks
Enter the information about above word in I, O, X format: XIIXX
Number of possible words: 36
Possible words (only show the first 50 words)
doura     altar     agora     hilar     riyal     lidar     filar     pilar     tolar     alvar
rhyta     aport     hijra     amour     jowar     rioja     royal     rival     algor     mudra
volar     flora     aggro     ixora     hydra     moira     ultra     amort     ottar     gular
augur     rugal     polar     attar     molar     jumar

Enter the word you want to try: flora
Enter the information about above word in I, O, X format: XXOOO
Number of possible words: 2
Possible words (only show the first 50 words)
agora     ixora

Enter the word you want to try: agora
Enter the information about above word in I, O, X format: OOOOO
Number of possible words: 1
Possible words (only show the first 50 words)
agora

Only possible word = agora
```
