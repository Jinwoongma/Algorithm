def solution(lines):
    answer = 0
    T = [0] * 90000000
    for line in lines:
        date, time, interval = line.split()
        h, m, s = time.split(':')
        s, ms = s.split('.')
        h, m, s, ms = int(h), int(m), int(s), int(ms)

        if '.' in interval:
            interval_s, interval_ms = map(int, interval[:-1].split('.'))
        else:
            interval_s, interval_ms = int(interval[:-1]), 0
        # print(h, m, s, ms, interval_s, interval_ms)

        end_idx = (((1000 * s) + ms) * m) * h
        interval_idx = (1000 * interval_s) + interval_ms
        start_idx = end_idx - interval_idx + 1
        if start_idx < 0:
            start_idx = 0

        print(start_idx, end_idx + 1000)
        for i in range(start_idx, end_idx + 1001):

            T[i] += 1
            answer = max(answer, T[i])

    return answer

solution([
    '2016-09-15 01:00:04.002 2.0s',
    '2016-09-15 01:00:07.000 2s'
    ])

