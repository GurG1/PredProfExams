class Songs:
    song_name = ''
    artist = ''
    qsongs = 0
    dtsongs = ''

f = open('songs.csv')
songs = []
j = 0
skip = f.readline()

for i in f:
    s = i.split(',')
    if (int(s[3][:-1])) == 01.01.2002:
        songs.append(Songs())
        songs[j].artist = s[1]
        songs[j].song_name = s[2]
        songs[j].qsongs = int(s[0])
        songs[j].dtsongs = s[3]
        j+=1

for i in range(len(songs)):
    j = 1
    t = songs[i]
    while j > 0 and songs[j-1] < t.dtsongs:
        songs[j] = songs[j-1]
        j-=1
    songs[j] = t