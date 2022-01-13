#!/usr/bin/env python3


import re


def read_data(name):
    '''Reads in the data of the provided subreddit.'''
    with open(name, encoding='utf8') as file:
        data = file.readlines()
        dict_list = [eval(line.rstrip()) for line in data]
    return dict_list


def find_triggers(data):
    '''Finds all user reminders in the provided data.'''
    triggers = []
    for line in data:
        temp = []
        for k, v in line.items():
            if k == 'body':
                if re.findall(r'(?i)(!remindme)', v) != [] or re.findall(r'(?i)(remindme!)', v) != []:
                    temp.append(v)
                    if re.findall(r'(?i)(!remindme)', v) != []:
                        temp.append(re.findall(r'(?i)(!remindme)', v))
                    else:
                        temp.append(re.findall(r'(?i)(remindme!)', v))
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
    '''Calculates the total amount of posts (comments) on the subreddit,
    the total amount of times someone wants to be reminded, and the
    amount someone replies after a reminder.'''
    # 0 = author, 1 = body, 2 = tagged mensen, 3 = created at, 4 = id van topic
    total_posts = 0
    total_reminds = 0
    total_replies = 0
    for post in triggers:
        total_posts += 1
        if post[2] != '':
            total_reminds += 1
            usernames = post[2]
            for name in usernames:
                for post2 in triggers:
                    if post2[4] == post[4] and post2[3] > post[3] and post2[0] == name[3:]:
                        total_replies += 1
                        #print(post2)
                        #print(name)
                        #print(post)
    return total_posts, total_reminds, total_replies


def main():
    gro_comments = read_data('Groningen_comment_1641290564.txt')
    gro_posts = read_data('Groningen_submission_1641290452.txt')
    bit_comments = read_data('BitMarket_comment_1641293337.txt')
    bit_posts = read_data('BitMarket_submission_1641293058.txt')

    triggers_gro = find_triggers(gro_comments)
    triggers_bit = find_triggers(bit_comments)
    posts, tags, replies = calculate_triggers(triggers_gro)
    print(posts, tags, replies)

    posts, tags, replies = calculate_triggers(triggers_bit)
    print(posts, tags, replies)


if __name__ == "__main__":
    main()