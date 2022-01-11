#!/usr/bin/env python3


import re


def read_data(name):
    '''Reads in the data of the provided subreddit.'''
    with open(name, encoding='utf8') as file:
        data = file.readlines()
        dict_list = [eval(line.rstrip()) for line in data]
    return dict_list


def find_triggers(data):
    '''Finds all user highlights and the corresponding data.'''
    triggers = []
    for line in data:
        temp = []
        for k, v in line.items():
            if k == 'body':
                if re.findall(r'(\/u\/\w+)', v) != []:
                    temp.append(v)
                    temp.append(re.findall(r'(\/u\/\w+)', v))
                else:
                    temp.append(v)
                    temp.append('')
            elif k == 'created_utc':
                temp.append(v)
            elif k == 'author':
                temp.append(v)
            elif k == 'link_id':
                temp.append(v)
        triggers.append(temp)
    return triggers


def calculate_triggers(triggers):
    '''Calculates the total amount of posts of on the subreddit,
    the total amount of times someone is tagged and the total
    amount someone replies to a tag.'''
    # 0 = author, 1 = body, 2 = tagged mensen, 3 = created at, 4 = id van topic
    total_posts = 0
    total_tags = 0
    total_replies = 0
    for post in triggers:
        total_posts += 1
        if post[2] != '':
            total_tags += 1
            usernames = post[2]
            for name in usernames:
                for post2 in triggers:
                    if post2[4] == post[4] and post2[3] > post[3] and post2[0] == name[3:]:
                        total_replies += 1
                        #print(post2)
                        #print(name)
                        #print(post)
    return total_posts, total_tags, total_replies


def main():
    data = read_data('Groningen_comment_1641290564.txt')
    triggers = find_triggers(data)
    posts, tags, replies = calculate_triggers(triggers)
    print(posts, tags, replies)


if __name__ == "__main__":
    main()