from collections import deque


def pers_is_select(name):
    return name[-1] == 'm'

def search_graf(name):
    search_queue = deque()
    search_queue += graf[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if pers_is_select(person):
                print(f'{person} is a mango seller')
                return True
            else:
                search_queue += graf[person]
                searched.append(person)
    return False


if __name__ == '__main__':

    graf = dict()
    graf['you'] = ['alice', 'bob', 'clara']
    graf['bob'] = ['anuj', 'peggy']
    graf['alice'] = ['peggy']
    graf['clara'] = ['tom', 'jonny']
    graf['anuj'] = []
    graf['peggy'] = []
    graf['tom'] = []
    graf['jonny'] = []
    search_graf('you')