def generateDocument(characters, document):
    # Write your code here.
    characters = characters.lower()
    document = document.lower()
    print(sorted(characters))
    print(sorted(document))
    if sorted(characters) == sorted(document):
        return True
    return False
    #return False

if __name__ == '__main__':
    characters = "Bste!hetsi ogEAxpelrt x "
    document = "AlgoExpert is the Best!"
    #generateDocument(characters,document)
    print(generateDocument(characters,document))