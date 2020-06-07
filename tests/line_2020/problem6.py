from collections import defaultdict
def tree(): return defaultdict(tree)

def add(t, path):
    for node in path:
        t = t[node]

def solution(directory, command):
    answer = []
    t = tree()
    for dir in directory:
        dir_lst = dir.split('/')
        dir_lst[0] = '/'
        print(dir_lst)
        add(t, dir_lst)
    print(t)
    return t

directory = [
    "/",
    "/hello",
    "/hello/tmp",
    "/root",
    "/root/abcd",
    "/root/abcd/etc",
    "/root/abcd/hello"
]

command = [
    "mkdir /root/tmp",
    "cp /hello /root/tmp",
    "rm /hello"
]

print(solution(directory, command))