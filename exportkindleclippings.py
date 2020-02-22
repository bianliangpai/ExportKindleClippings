import sys

def is_similarly(note1 = '', note2 = ''):
    if len(note1) >= len(note2):
        return note1[:len(note2)] == note2
    else:
        return note1 == note2[:len(note1)]


def readclippings(clippingspath = 'My Clippings.txt'):
    f=open(clippingspath,'r+', encoding='UTF-8-sig')
    clippingnotes = {}

    while True:
        onenote=[]
        for _ in range(0,5):
            line = f.readline()
            if not line:
                return clippingnotes
            line = line.rstrip('\n')
            onenote.append(line)

        # put into dict
        curnote = onenote[3]
        bookpath = onenote[0]+'.txt'
        if not clippingnotes.get(bookpath):
            clippingnotes[bookpath] = []
        if not clippingnotes[bookpath]:
            clippingnotes[bookpath].append(curnote)
        elif not is_similarly(clippingnotes[bookpath][-1], curnote):
            clippingnotes[bookpath].append(curnote)
        else:
            clippingnotes[bookpath][-1] = curnote
            


def writenotes(clippingnotes = {}):
    for book, notes in clippingnotes.items():
        booknote = open(book,'a+', encoding='UTF-8')
        for note in notes:
            booknote.write(note+'\n')
        booknote.close()


if __name__ == "__main__":

    if len(sys.argv) > 1:
        clippingnotes = readclippings(sys.argv[1])
    else:
        clippingnotes = readclippings()
    
    writenotes(clippingnotes)