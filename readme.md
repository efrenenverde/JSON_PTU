## Personal python practice project

The PDF to Json transformation is done over at https://www.pdf2go.com/es
Some slight modifications are required:
* We need to remove all previous info pages, so the document starts with the first pokemon registry
* For the program to recognice the complete text we need to remove the double quotation marks used in the size information section of each pokemon and the § symbol from the movelists that have that. (Ctrl+f and replace to delete them all at once)
