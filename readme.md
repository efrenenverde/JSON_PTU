## PTU Pokedex to Json

This proyect started as a practice run for me to get used to Python, if you look into the code it's evidently clear how I learned and improved my methods as I got deeper into it some of it is just plainly bad. You may notice that this git repository is not that old, but that's because I run into a serious problem a while ago and thought I needed to start from scratch so I deleted the repository, only to later find a solution and finally finishing it.

The objective of this proyect is to create a database on MongoDB with up to date information from the tabletop game "Pokemon Tabletop United", an unofficial game developed by fans, to be used in a larger proyect of creating an easier way to access the information from the books with the intention to make this great games more accessible to veterans and new commers.

The file "finalJson.txt" is formatted in a way that allows to simply copy-paste it's content into Robo 3T's Insert Document functionality. 

The PDF to Json transformation is done over at https://www.pdf2go.com/es
Some slight modifications are required:
* We need to remove all previous info pages, so the document starts with the first pokemon registry
* For the program to recognice the complete text we need to remove the double quotation marks used in the size information section of each pokemon and the § symbol from the movelists that have that. (Ctrl+f and replace to delete them all at once)
* After finding a critical problem with the formatting of many TM Move Lists on different pokemon I attempted to re-do the program accessing the data directly with a python PDF reader, it had it's own critical flaws so I decided to come back to this version and manually edit both files in DATA to make sure the TM Move List was a continuous block.
* In the same fashion as the issue with the discontinous TM Move List, some Egg Move Lists mut be edited. Many less tho.
* For some reason the txt didnt get the Breeding information on some Galar pokemon, thus it had to be added manually.
* Some Galar pokemon need to get their Breeding Information copied manually on to the Data file because it was not copied correctly