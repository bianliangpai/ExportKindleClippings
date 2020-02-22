import sys

def print_usage():
    print('usage:')
    print('  python exportkindleclippings.py path/to/My Clippings.txt\n')

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
        # kindle默认每一条笔记会在'My Clippings.txt'里产生5行记录
        # 其中第1行为文件名，第4行为实际需要的记录
        for _ in range(0,5):
            line = f.readline()
            if not line:
                return clippingnotes
            line = line.rstrip('\n')
            onenote.append(line)

        curnote = onenote[3]
        bookpath = onenote[0]+'.txt'
        if not clippingnotes.get(bookpath):
            clippingnotes[bookpath] = []
        if not clippingnotes[bookpath]:
            clippingnotes[bookpath].append(curnote)
        # 在kindle内选择笔记时，由于跨页、系统卡顿等原因，笔记的选择范围经常会不太精确
        # 由于kindle会把所有误操作的笔记也写进My Clippings.txt里，为方便整理，这里去掉了这些重复记录
        elif is_similarly(clippingnotes[bookpath][-1], curnote):
            clippingnotes[bookpath][-1] = curnote
        else:
            clippingnotes[bookpath].append(curnote)
            


def writenotes(clippingnotes = {}):
    for book, notes in clippingnotes.items():
        booknote = open(book,'a+', encoding='UTF-8')
        for note in notes:
            booknote.write(note+'\n')
        booknote.close()


if __name__ == "__main__":

    print_usage()

    if len(sys.argv) > 1:
        clippingnotes = readclippings(sys.argv[1])
    else:
        clippingnotes = readclippings()
    
    writenotes(clippingnotes)