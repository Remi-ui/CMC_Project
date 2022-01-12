import json
import ast
import re

def main():
    
    f = open('Groningen_comment_1641290564.txt', 'r')
    cnt = 0
    prev_link = ''
    auth_list = []
    for line in f:
        cnt += 1
        #print(cnt)
        json_dat = json.dumps(ast.literal_eval(line))
        dict_dat = json.loads(json_dat)

        author = dict_dat['author']
        if 'permalink' in dict_dat:
            or_link = dict_dat['permalink']
            link = or_link.rsplit('/', 2)
            link = link[0] 
        else:
            link = "NO LINK" 
        message = dict_dat['body']
        if link == prev_link or prev_link == '':
            auth_list.append(author)
        user = re.findall(r"/u/[A-Za-z0-9_-]+", message)
        
        if len(user) != 0:
            for person in user:
                person = person.replace('/u/','')
                if person not in auth_list:
                    print("")
                    print('----------')
                    print(link)
                    print(or_link)
                    print(message)
                    print('----------')

        prev_link = link

if __name__ == "__main__":
    main()


# p = open('Groningen_comment_1641290564.txt', 'r')
#             cnt_inner = 0
#             for entry in p:
#                 #print(cnt)
#                 cnt_inner += 1
#                 #print(cnt_inner)
#                 #print(cnt_inner)
#                 json_dat = json.dumps(ast.literal_eval(entry))
#                 dict_dat = json.loads(json_dat)
#                 if 'permalink' in dict_dat:
#                     cur_link = dict_dat['permalink']
#                     cur_link = cur_link.rsplit('/', 2)
#                     cur_link = cur_link[0] 
#                 if cur_link == link:
#                     if dict_dat['author'] in user_u and cnt_inner < cnt:
#                         print("nee!")
#                     elif dict_dat['author'] in user_u and cnt_inner > cnt:
#                         print(cur_link)
#                         print("ja!")
#                         print(dict_dat['body'])