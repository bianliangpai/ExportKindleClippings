import sys

def print_usage():
    print('')
    print('usage:\n  python exportkindleclippings.py path/to/My Clippings.txt')
    print("default clippings path:\n  ./My Clippings.txt\n")

def is_similarly(note1 = '', note2 = ''):
    if note1 != '' and note2 != '':
        if len(note1) >= len(note2):
            return note2 in note1
        else:
            return note1 in note2
    else:
        return False

def get_real_note(onenote):
    # 一条记录中默认第1行为文件名，第2行为辅助信息，剩下的信息为实际记录
    onenote = onenote[2:]
    while '' in onenote:
        onenote.remove('')
    if len(onenote) > 0:
        return onenote[0]
    else:
        return ''

def make_book_name_valid(bookname):
    for char in ':/':
        while char in bookname:
            bookname = bookname.replace(char, '_')
    return bookname

def readclippings(clippingspath):
    try:
        with open(clippingspath,'r+', encoding='utf-8-sig') as f:
            clippingnotes = {}
            while True:
                onenote = []
                # kindle默认每两条笔记之间的分割为 ==========
                while True:
                    line = f.readline()
                    if not line:
                        return clippingnotes
                    line = line.encode('utf-8').decode('utf-8-sig').rstrip('\n')
                    if line == '==========':
                        break
                    onenote.append(line)

                realnote = get_real_note(onenote)
                if realnote == '':
                    continue

                bookpath = onenote[0]+'.txt'
                if not clippingnotes.get(bookpath):
                    clippingnotes[bookpath] = []
                if not clippingnotes[bookpath]:
                    clippingnotes[bookpath].append(realnote)
                # 在kindle内选择笔记时，由于跨页、系统卡顿等原因，笔记的选择范围经常会不太精确
                # 由于kindle会把所有误操作的笔记也写进My Clippings.txt里，为方便整理，这里去掉了这些重复记录
                else:
                    for note in clippingnotes[bookpath]:
                        if is_similarly(note, realnote):
                            note = realnote
                            break
                    else:
                        clippingnotes[bookpath].append(realnote)
    except IOError:
        print("clipping file not exist!")


def writenotes(clippingnotes = {}):
    for book, notes in clippingnotes.items():
        book = make_book_name_valid(book)
        result_path = 'result/'+book
        booknote = open(result_path,'w+', encoding='utf-8')
        print('writing notes of %s' % book[:-4])
        for note in notes:
            booknote.write(note+'\n')
        booknote.close()


if __name__ == "__main__":

    print_usage()

    if len(sys.argv) > 1:
        clippingnotes = readclippings(sys.argv[1])
    else:
        clippingnotes = readclippings('My Clippings.txt')
    print("finished reading 'My Clippings.txt'\n")
    
    writenotes(clippingnotes)
    print('\ndone')