#!/usr/bin/env python3


def read_data(name):
    '''Reads in the data of the provided subreddit.'''
    with open(name, encoding='utf8') as file:
        data = file.readlines()
        dict_list = [eval(line.rstrip()) for line in data]
    return dict_list


def find_metavoicing(comments, posts):
    total_comments = len(comments)
    total_posts = len(posts)
    total_karma = 0
    print('Total posts and total comments:', total_posts, total_comments)
    print('Comments per posts:', round(total_comments / total_posts, 3))

    for line in comments:
        for k, v in line.items():
            if k == 'score':
                total_karma += v
    for line in posts:
        for k, v in line.items():
            if k == 'score':
                total_karma += v
    print(total_karma)

    return total_comments, total_posts


def main():
    gro_comments = read_data('Groningen_comment_1641290564.txt')
    gro_posts = read_data('Groningen_submission_1641290452.txt')
    bit_comments = read_data('BitMarket_comment_1641293337.txt')
    bit_posts = read_data('BitMarket_submission_1641293058.txt')
    find_metavoicing(gro_comments, gro_posts)
    find_metavoicing(bit_comments, bit_posts)

if __name__ == "__main__":
    main()