import json
import ast
import re

def main():
    
    f = open('BitMarket_comment_1641293337.txt', 'r')
    auth_comment = set()
    auth_submission = set()
    for line in f:
        json_dat = json.dumps(ast.literal_eval(line))
        dict_dat = json.loads(json_dat)

        author = dict_dat['author']
        auth_comment.add(author)

    f = open('BitMarket_submission_1641293058.txt', 'r')
    for line in f:
        json_dat = json.dumps(ast.literal_eval(line))
        dict_dat = json.loads(json_dat)

        author = dict_dat['author']
        auth_submission.add(author)

    overlap = auth_comment.intersection(auth_submission)
    print("Number of unique authors that created a post: {}".format(len(auth_submission)))
    print("Number of unique authors that made a comment: {}".format(len(auth_comment)))
    print("Overlap: {}".format(len(overlap)))

if __name__ == "__main__":
    main()