import json
import ast
import re

def main():
    
    f = open('BitMarket_comment_1641293337.txt', 'r')
    cnt = 0
    total = 0
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
                if person not in auth_list and author!='AutoModerator' and or_link != '/r/BitMarket/comments/78c4y2/wts_mint_or_nearly_mint_oj_simpson_rookie_card/dosnnc9/' and or_link != '/r/BitMarket/comments/7ky6xb/scammer_urezrami/drk59vq/' and link != '/r/BitMarket/comments/8timox/wts_adobe_creative_cloud_all_apps_adobe_stock':
                    total += 1
                    print("")
                    print('----------')
                    print(link)
                    print(or_link)
                    print(message)
                    print(total)
                    print('----------')

        prev_link = link

if __name__ == "__main__":
    main()