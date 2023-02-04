### Packages
from facebook_scraper import get_posts
import pandas as pd
from datetime import datetime
import warnings 
from random import randint
from time import sleep
import os
import sys
import time


### Param
try:
    fanpage = sys.argv[1]
    cookie_num = int(sys.argv[2])
except IndexError:
    print("Please input a fanpage")

P = pd.DataFrame()
page_default = 200 # for test: 3 / for formal: 200
#cookie_num = 1
i=0 # count posts




### Main
print(fanpage)
for post in get_posts(fanpage, pages=page_default, cookies = "cookies/facebook.com_cookies_{}.txt".format(cookie_num), options={"reactors": True}):
    try:
        #print(post['post_text'] == post['text'])
        print(post['reactions'])
        print(post['likes'])
        localtime = time.localtime()
        result = time.strftime("%Y-%m-%d %H:%M:%S ", localtime)
        print(result)
        #print(post)
        if int(post['time'].strftime("%Y")) <= 2019: break
        if "{}.xlsx".format(fanpage) in os.listdir("./output"):
            print("Duplicated!")
            break
        if post['likes'] is not None:
            P = P.append(
                {'user_id'        : str(post['user_id']),
                 'username'       : str(post['username']),
                 'time'           : post['time'],
                 'post_url'       : post['post_url'],
                 'post_id'        : str(post['post_id']),
                 'post_text'      : post['post_text'].strip().replace("\n", ""),
                 'like_count'     : post['likes'],
                 'love_count'     : 0,
                 'go_count'       : 0,
                 'wow_count'      : 0,
                 'haha_count'     : 0,
                 'sad_count'      : 0,
                 'angry_count'    : 0,
                 'share_count'    : post['comments'],
                 'comment_count'  : post['shares'],
                 'videoUrl'          : "No"  if post['video'] is None else str(post['video']),
                 'imageUrl'          : "No"  if len(post ['images_lowquality']) == 0 else post ['images_lowquality'],
                },ignore_index=True)
            warnings.filterwarnings( "ignore" )
            i = i + 1
            print("\n\t> DONE{}.....POST_ID: {}  {}\n\t>>>>> {}\n\n".format(i, str(post['post_id']), str(post['time']), str(post['post_url'])))
            sleep(randint(30,90))
            continue
        elif post ['reactions'] == None and post ['images_lowquality'] is not None and post ['post_text'] is not None: # 可能 reaction 欄位失效出錯
            P = P.append(
                {'user_id'        : str(post['user_id']),
                 'username'       : str(post['username']),
                 'time'           : post['time'],
                 'post_url'       : post['post_url'],
                 'post_id'        : str(post['post_id']),
                 'post_text'      : post['post_text'].strip().replace("\n", ""),
                 'like_count'     : 0,
                 'love_count'     : 0,
                 'go_count'       : 0,
                 'wow_count'      : 0,
                 'haha_count'     : 0,
                 'sad_count'      : 0,
                 'angry_count'    : 0,
                 'share_count'    : post['comments'],
                 'comment_count'  : post['shares'],
                 'videoUrl'          : "No"  if post['video'] is None else str(post['video']),
                 'imageUrl'          : "No"  if len(post ['images_lowquality']) == 0 else post ['images_lowquality'],
                },
                ignore_index=True)
            warnings.filterwarnings( "ignore" )
            i = i + 1
            print("\n\t>> DONE{}.....POST_ID: {}  {}\n\t>>>>> {}\n\n".format(i, str(post['post_id']), str(post['time']), str(post['post_url'])))
            sleep(randint(30,90))
            continue
        elif post ['reactions'] == None and post ['images_lowquality'] is None and post ['post_text'] is not None: # 可能 images_lowquality 欄位失效出錯
            P = P.append(
                {'user_id'        : str(post['user_id']),
                 'username'       : str(post['username']),
                 'time'           : post['time'],
                 'post_url'       : post['post_url'],
                 'post_id'        : str(post['post_id']),
                 'post_text'      : post['post_text'].strip().replace("\n", ""),
                 'like_count'     : 0,
                 'love_count'     : 0,
                 'go_count'       : 0,
                 'wow_count'      : 0,
                 'haha_count'     : 0,
                 'sad_count'      : 0,
                 'angry_count'    : 0,
                 'share_count'    : post['comments'],
                 'comment_count'  : post['shares'],
                 'videoUrl'          : "No"  if post['video'] is None else str(post['video']),
                 'imageUrl'          : "No"  if len(post ['images_lowquality']) == 0 else post ['images_lowquality'],
                },
                ignore_index=True)
            warnings.filterwarnings( "ignore" )
            i = i + 1
            print("\n\t>>> DONE{}.....POST_ID: {}  {}\n\t>>>>> {}\n\n".format(i, str(post['post_id']), str(post['time']), str(post['post_url'])))
            sleep(randint(30,90))
            continue
        elif post ['images_lowquality'] is None and post ['post_text'] is not None:
            P = P.append(
                {'user_id'        : str(post['user_id']),
                 'username'       : str(post['username']),
                 'time'           : post['time'],
                 'post_url'       : post['post_url'],
                 'post_id'        : str(post['post_id']),
                 'post_text'      : post['post_text'].strip().replace("\n", ""),
                 'like_count'     : post ['reactions']['讚']   if '讚' in post['reactions'].keys() else 0,
                 'love_count'     : post ['reactions']['大心']  if '大心' in post['reactions'].keys() else 0,
                 'go_count'       : post ['reactions']['加油'] if '加油' in post['reactions'].keys() else 0,
                 'wow_count'      : post ['reactions']['哇']   if '哇' in post['reactions'].keys() else 0,
                 'haha_count'     : post ['reactions']['哈']   if '哈' in post['reactions'].keys() else 0,
                 'sad_count'      : post ['reactions']['嗚']   if '嗚' in post['reactions'].keys() else 0,
                 'angry_count'    : post ['reactions']['怒']   if '怒' in post['reactions'].keys() else 0,
                 'share_count'    : post['comments'],
                 'comment_count'  : post['shares'],
                 'videoUrl'          : "No"  if post['video'] is None else str(post['video']),
                 'imageUrl'          : "No",
                },
                ignore_index=True)
            warnings.filterwarnings( "ignore" )
            i = i + 1
            print("\n\t>>>> DONE{}.....POST_ID: {}  {}\n\t>>>>> {}\n\n".format(i, str(post['post_id']), str(post['time']), str(post['post_url'])))
            sleep(randint(30,90))
            continue
        elif post ['post_text'] is None:
            P = P.append(
                {'user_id'        : str(post['user_id']),
                 'username'       : str(post['username']),
                 'time'           : post['time'],
                 'post_url'       : post['post_url'],
                 'post_id'        : str(post['post_id']),
                 'post_text'      : "",
                 'like_count'     : post ['reactions']['讚']   if '讚' in post['reactions'].keys() else 0,
                 'love_count'     : post ['reactions']['大心']  if '大心' in post['reactions'].keys() else 0,
                 'go_count'       : post ['reactions']['加油'] if '加油' in post['reactions'].keys() else 0,
                 'wow_count'      : post ['reactions']['哇']   if '哇' in post['reactions'].keys() else 0,
                 'haha_count'     : post ['reactions']['哈']   if '哈' in post['reactions'].keys() else 0,
                 'sad_count'      : post ['reactions']['嗚']   if '嗚' in post['reactions'].keys() else 0,
                 'angry_count'    : post ['reactions']['怒']   if '怒' in post['reactions'].keys() else 0,
                 'share_count'    : post['comments'],
                 'comment_count'  : post['shares'],
                 'videoUrl'          : "No"  if post['video'] is None else str(post['video']),
                 'imageUrl'          : "No",
                },
                ignore_index=True)
            warnings.filterwarnings( "ignore" )
            i = i + 1
            print("\n\t>>>>> DONE{}.....POST_ID: {}  {}\n\t>>>>> {}\n\n".format(i, str(post['post_id']), str(post['time']), str(post['post_url'])))
            sleep(randint(30,90))
            continue
        P = P.append(
            {'user_id'        : str(post['user_id']),
             'username'       : str(post['username']),
             'time'           : post['time'],
             'post_url'       : post['post_url'],
             'post_id'        : str(post['post_id']),
             'post_text'      : post['post_text'].strip().replace("\n", ""),
             'like_count'     : post ['reactions']['讚']   if '讚' in post['reactions'].keys() else 0,
             'love_count'     : post ['reactions']['大心']  if '大心' in post['reactions'].keys() else 0,
             'go_count'       : post ['reactions']['加油'] if '加油' in post['reactions'].keys() else 0,
             'wow_count'      : post ['reactions']['哇']   if '哇' in post['reactions'].keys() else 0,
             'haha_count'     : post ['reactions']['哈']   if '哈' in post['reactions'].keys() else 0,
             'sad_count'      : post ['reactions']['嗚']   if '嗚' in post['reactions'].keys() else 0,
             'angry_count'    : post ['reactions']['怒']   if '怒' in post['reactions'].keys() else 0,
             'share_count'    : post['comments'],
             'comment_count'  : post['shares'],
             'videoUrl'          : "No"  if post['video'] is None else str(post['video']),
             'imageUrl'          : "No"  if len(post ['images_lowquality']) == 0 else post ['images_lowquality'],

            },
        ignore_index=True)
        warnings.filterwarnings( "ignore" )
        i = i + 1
        print("\n\t|>>>>>> DONE{}.....POST_ID: {}  {}\n\t>>>>> {}\n\n".format(i, str(post['post_id']), str(post['time']), str(post['post_url'])))
        #print(P)
        sleep(randint(30,90))
        continue
        #if i == 134:
        #    P.to_excel("./{}.xlsx".format(fanpage), sheet_name='sheet1', index=False)
        #    P.to_csv("./{}.csv".format(fanpage), index=False, encoding='utf-8')
    except:
        print("\n\t|||| ERROR{}.....POST_ID: {}  {}\n\t>>>>> {}\n\n".format(i, str(post['post_id']), str(post['time']), str(post['post_url'])))
        P.to_excel("./新增爬蟲/{}_{}ERROR.xlsx".format(fanpage,i), sheet_name='sheet1', index=False)
        P.to_csv("./新增爬蟲/{}_{}ERROR.csv".format(fanpage,i), index=False, encoding='utf-8')
        break





### Write Files
if "{}.xlsx".format(fanpage) not in os.listdir("./output"):
    P.to_excel("./新增爬蟲/{}.xlsx".format(fanpage), sheet_name='sheet1', index=False)
    P.to_csv("./新增爬蟲/{}.csv".format(fanpage), index=False, encoding='utf-8')
