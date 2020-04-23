## Personal python practice project

The PDF to Json transformation is done over at https://www.pdf2go.com/es
Some slight modifications are required:
* We need to remove all previous info pages, so the document starts with the first pokemon registry
* For the program to recognice the complete text we need to remove the double quotation marks used in the size information section of each pokemon and the § symbol from the movelists that have that. (Ctrl+f and replace to delete them all at once)
* After finding a critical problem with the formatting of many TM Move Lists on different pokemon I attempted to re-do the program accessing the data directly with a python PDF reader, it had it's own critical flaws so I decided to come back to this version and manually edit both files in DATA to make sure the TM Move List was a continuous block.
* In the same fashion as the issue with the discontinous TM Move List, some Egg Move Lists mut be edited. Many less tho.