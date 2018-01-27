
har_drive = 'my.song.mp3 11b, \
       reat.flac 1000b, \
       not3.text 5b, \
       video.mp4 200b, \
       game.exe 100b, \
       mov!e.mkv 10000b'





def extract_mp3(data):
    start = data.find('mp3')
    see_num = data.find(' ',start)
    end_read = data.find('b',see_num)
    return data [see_num+ 1 : end_read]

def extract_flac(data):
    start = data.find('flac')
    see_num = data.find(' ',start)
    end_read = data.find('b',see_num)
    return data [see_num+ 1 : end_read]

def extract_mp4(data):
    start = data.find('mp4')
    see_num = data.find(' ',start)
    end_read = data.find('b',see_num)
    return data [see_num+ 1 : end_read]


def extract_mkv(data):
    start = data.find('mkv')
    see_num = data.find(' ',start)
    end_read = data.find('b',see_num)
    return data [see_num+ 1 : end_read]


def extract_text(data):
    start = data.find('text')
    see_num = data.find(' ',start)
    end_read = data.find('b',see_num)
    return data [see_num+ 1 : end_read]

def extract_exe(data):
    start = data.find('exe')
    see_num = data.find(' ',start)
    end_read = data.find('b',see_num)
    return data [see_num+ 1 : end_read]




musics = str(int(extract_mp3(har_drive)) + int(extract_flac(har_drive))) + 'b'

images= '0b'

movies = str(int(extract_mp4(har_drive)) + int(extract_mkv(har_drive))) + 'b'

others = str(int(extract_exe(har_drive)) + int(extract_text(har_drive))) + 'b'

solution = 'music '+ musics + ', '+'images '+ images +', '+'movies '+ movies +', '+'others '+ others


print (solution)
    
