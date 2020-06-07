def solution(m, musicinfos):
    answer = ''
    dic = {}
    m_list = []
    for c in m:
        if c == '#':
            m_list[-1] += '#'
        else:
            m_list.append(c)
    m_list = tuple(m_list)

    for music_info in musicinfos:
        st, et, name, music = music_info.split(',')
        sh, sm = map(int, st.split(':'))
        eh, em = map(int, et.split(':'))
        interval = (eh * 60 + em) - (sh * 60 + sm)

        music_list = []
        for c in music:
            if c == '#':
                music_list[-1] += '#'
            else:
                music_list.append(c)

        L = len(music_list)
        if interval > L:
            music_list *= (interval // L)
            music_list += music_list[:interval % L]
        else:
            music_list = music_list[:interval]
        music = tuple(music_list)
        dic[music] = name

    answer_music = ''
    for music in dic:
        for i in range(len(music) - len(m_list) + 1):
            if music[i:i + len(m_list)] == m_list:
                if answer != '' and len(music) > len(answer_music):
                    answer = dic[music]
                    answer_music = music
                else:
                    answer = dic[music]
                    answer_music = music

    if answer == '':
        return '(None)'
    else:
        return answer

