import json
import os
import execjs
import requests
import time
from pathlib import Path
from tqdm import tqdm

# 检测运行环境
if not any("\\nodejs" in i for i in os.getenv('path').split(";")):
    # node地址
    f_luj = os.path.join(Path.cwd(),"nodejs")
    # 获取当前用户的环境变量以便追加
    os.system(f'reg query "HKCU\\Environment" -v Path > temp.txt')
    user_path = Path('temp.txt').read_text().replace("\n", "").replace("HKEY_CURRENT_USER\\Environment    Path    REG_SZ    ","")
    if user_path:
        os.system(f'setx Path "{user_path};{f_luj}" > temp.txt 2>&1')
    else:
        os.system(f'setx Path "{f_luj}" > temp.txt 2>&1')
    Path('temp.txt').unlink()
    input("已为你更新缺失的环境,请重新运行")
    exit()
# 定义运行目录
kesPath = Path(Path.cwd())
while True:
    try:
        user_serch = input("搜索:")
        # 头部信息
        cookies = {
            "pgv_pvid": "5175608000",
            "fqm_pvqid": "756ab1e0-7ffb-4cf8-8521-3901b01a9c4d",
            "ts_uid": "5501206530",
            "RK": "fWdIjGSj9C",
            "ptcz": "d230fb4b42abbfea19d7507b2f6fe03def99f72d685347a9831f8c820ffcd0da",
            "qq_domain_video_guid_verify": "42b2b9a07e3cf423",
            "_qimei_uuid42": "184061008301000413b32ab925da2c83aaf21db28d",
            "o_cookie": "2172093349",
            "_qimei_q36": "",
            "_qimei_h38": "b885d4e113b32ab925da2c8302000006618406",
            "o2_uin": "2172093349",
            "iip": "0",
            "LW_uid": "f1Y7p1t4q3m0z9O8B8i8w8v3i7",
            "eas_sid": "m1v7w124Z3I0w9r8S8k8C8C4x1",
            "_qimei_fingerprint": "5b7d4258a5cb4acd8852380bfbc478c0",
            "LW_sid": "w1B7U2E0T5Q069f4V3D8g7C8J6",
            "pac_uid": "0_3G5ipr7ZE8AWp",
            "suid": "user_0_3G5ipr7ZE8AWp",
            "ts_refer": "cn.bing.com/",
            "ptui_loginuin": "2172093349",
            "fqm_sessionid": "4307ebc2-7d3b-4a0e-aa90-0f1b93d988b3",
            "pgv_info": "ssid=s8259890548",
            "ts_last": "y.qq.com/",
            "_qpsvr_localtk": "0.15837268212550093",
            "login_type": "1",
            "psrf_access_token_expiresAt": "1733590530",
            "psrf_musickey_createtime": "1732985730",
            "psrf_qqopenid": "015446616C0769AF75CB3E298FFCA92D",
            "wxunionid": "",
            "euin": "ow6lownqoioPNv**",
            "uin": "2172093349",
            "psrf_qqaccess_token": "7F4A1CC4C89B03961154DCDA018CBA14",
            "wxrefresh_token": "",
            "qm_keyst": "Q_H_L_63k3N9HnPKgl-8_-1w2k9-eptByJ9Yi26buSVrIqFb1S1qkYcqHfKoMEw19daghTDpb4O8yl5tBeqdyR6wcWPC98k2DI",
            "psrf_qqunionid": "F4CBE8D100C1C5B50B88844D7E0FF7A1",
            "psrf_qqrefresh_token": "FB5D92B908AB1EF4727695B628CFE7CB",
            "qqmusic_key": "Q_H_L_63k3N9HnPKgl-8_-1w2k9-eptByJ9Yi26buSVrIqFb1S1qkYcqHfKoMEw19daghTDpb4O8yl5tBeqdyR6wcWPC98k2DI",
            "tmeLoginType": "2",
            "wxopenid": "",
            "music_ignore_pskey": "202306271436Hn@vBj"
        }
        headers = {
            'accept': 'application/json',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'content-type': 'application/x-www-form-urlencoded',
            'dnt': '1',
            'origin': 'https://y.qq.com',
            'priority': 'u=1, i',
            'referer': 'https://y.qq.com/',
            'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
        }


        ######################### 获取数据
        def req_info():
            # 生成searchid
            def searchid():
                fle = f'{kesPath}\\wordsJS\\searchid.js'
                with open(fle, 'r', encoding='utf-8') as f:
                    return execjs.compile(f.read()).eval('searchid')

            data = {
                "comm": {
                    "cv": 4747474,
                    "ct": 24,
                    "format": "json",
                    "inCharset": "utf-8",
                    "outCharset": "utf-8",
                    "notice": 0,
                    "platform": "yqq.json",
                    "needNewCode": 1,
                    "uin": 2172093349,
                },
                "req_1": {
                    "method": "DoSearchForQQMusicDesktop",
                    "module": "music.search.SearchCgiService",
                    "param": {
                        "remoteplace": "txt.yqq.center",
                        "searchid": "",
                        "search_type": 0,
                        "query": "",
                        "page_num": 1,
                        "num_per_page": 10
                    }
                }
            }
            data['req_1']['param']['searchid'] = searchid()
            data['req_1']['param']['query'] = user_serch
            data = json.dumps(data, ensure_ascii=False)

            # # 获取歌单的sign
            def sign():
                fle = f'{kesPath}\\wordsJS\\sign.js'
                with open(fle, 'r', encoding='utf-8') as f:
                    return execjs.compile(f.read()).call('sign', data)

            ########## 请求数据
            params = {
                '_': round(time.time() * 1000),
                'sign': sign(),
            }
            response = requests.post(
                'https://u6.y.qq.com/cgi-bin/musics.fcg',
                params=params,
                cookies=cookies,
                headers=headers,
                data=data.encode()
            ).json()
            return response


        # ######################## 清洗数据
        if req_info()['req_1']['data']['body']['song']['list'] == []:
            print("很抱歉，暂时没有找到相关的结果")
            continue
        edict = {
            'show_info': [],
            'dw_param': [],
        }
        ID_temp = 1
        oeoedd = req_info()['req_1']['data']['body']['song']['list'][0]
        let_ife = ''
        if len(oeoedd['title']) > 20 or len(oeoedd['album']['subtitle']) > 10 or len('/'.join(i['name'] for i in oeoedd['singer'])) > 15 or len(oeoedd['album']['name']) > 10:
            print("检测到歌曲信息长度过大,是否需要启用省略\n")
            let_ife = input("yes/no:")
        for listData in req_info()['req_1']['data']['body']['song']['list']:
            ########## 这是歌曲下载所需的参数
            mid = listData['mid']
            id = listData['id']
            album = listData['album']
            albumMid = album['mid']
            edict['dw_param'].append(
                {
                    "mid": mid,
                    "id": id,
                    "albumMid": albumMid
                }
            )
            ########## 这是歌曲基本信息
            # 歌名`
            music_title = listData['title']
            # 副标题
            music_title2 = album['subtitle']
            # 获取到一个对象  里面有音乐作者的一些参数
            singer = listData['singer']
            # 作者
            music_author = '/'.join(i['name'] for i in singer)
            # 专辑
            music_album = album['name']
            if let_ife == "yes":
                    if len(music_title) > 20:
                        music_title = music_title[:20] + '....'
                    if len(music_title2) > 10:
                        music_title2 = music_title2[:10] + '....'
                    if len(music_author) > 15:
                        music_author = music_author[:15] + '....'
                    if len(music_album) > 10:
                        music_album = music_album[:10] + '....'

            # 时长
            def musicDuration_item(e):
                D = e // 86400  # 剩余天   1天=86400秒
                H = e % 86400 // 3600  # 剩余时    1时=3600秒
                Min = e % 3600 // 60  # 剩余分
                S = e % 60  # 剩余秒
                if D < 10: D = "0" + str(D)
                if H < 10: H = "0" + str(H)
                if Min < 10: M = "0" + str(Min)
                if S < 10: S = "0" + str(S)
                return f'{Min}:{S}'


            # 将获取的秒放入musicDuration_item处理为时长
            music_Duration = musicDuration_item(listData['interval'])
            # 将数据传出到edict的show_info字典
            edict['show_info'].append(
                {
                    "序列ID": ID_temp,
                    "歌曲": music_title,
                    "相关": f'{music_title2}',
                    "作者": music_author,
                    "专辑": music_album,
                    "时长": music_Duration,
                }
            )
            # 序列ID号
            ID_temp += 1
        # ####################### 使用PrettyTable库制作表格展示
        from prettytable import PrettyTable, DOUBLE_BORDER

        table = PrettyTable()
        table.set_style(DOUBLE_BORDER)
        table.hrules = True
        table.field_names = edict['show_info'][0].keys()
        for i in edict['show_info']:
            table.add_row(i.values())
        table.align["歌曲名字"] = "l"
        print(table)


        # ############################## 下载歌曲功能模块
        def req_DW():
            """
            # 关于表单加密
            # 其中变化的参数有: songMID  songID biz_id  albumMid  guid songmid
            #  songMID 的值和 songmid 的值一样   已找到  原来的mid就是它们
            #  songID 和 biz_id 一样  已找到    原来的id就是它们
            # albumMid     已找到    原来的 album里面的 mid就是它
            # guid   未找到    估计是js生成的 是一直变化的
            # =================================以上是data的参数分析
            # 关于参数加密有:sign _
            其中 _  是一个时间戳
            sign   调试发现sign是通过data表单加密的参数 因为data表单是变化的,所以sign也是随表单变化的
            """
            ############### 获取参数用于修改表单
            datalist = []
            for par_dist, main_info in zip(edict['dw_param'], edict['show_info']):
                # 获取 songMID和songmid   它们是一样的都是原来的mid
                mid = par_dist['mid']
                # 获取 songID 和 biz_id   它们是一样的都是原来的id
                pid = par_dist['id']
                # albumMid
                albumMid = par_dist['albumMid']

                # 获取guid
                def guid():
                    fle = f'{kesPath}\\wordsJS\\guid.js'
                    return execjs.compile(Path(fle).read_text()).call('guid')

                # print(mid,pid,albumMid,guid())
                dataDW = {
                    "comm": {
                        "cv": 4747474,
                        "ct": 24,
                        "format": "json",
                        "inCharset": "utf-8",
                        "outCharset": "utf-8",
                        "notice": 0,
                        "platform": "yqq.json",
                        "needNewCode": 1,
                        "uin": 2172093349,
                        "g_tk_new_20200303": 550468887,
                        "g_tk": 550468887
                    },
                    "req_1": {
                        "module": "music.musichallSong.PlayLyricInfo",
                        "method": "GetPlayLyricInfo",
                        "param": {
                            "songMID": "003S1hgM2asCye",
                            "songID": 102174489
                        }
                    },
                    "req_2": {
                        "method": "GetCommentCount",
                        "module": "music.globalComment.GlobalCommentRead",
                        "param": {
                            "request_list": [
                                {
                                    "biz_type": 1,
                                    "biz_id": "102174489",
                                    "biz_sub_type": 0
                                }
                            ]
                        }
                    },
                    "req_3": {
                        "module": "music.musichallAlbum.AlbumInfoServer",
                        "method": "GetAlbumDetail",
                        "param": {
                            "albumMid": "003c616O2Zlswm"
                        }
                    },
                    "req_4": {
                        "module": "music.vkey.GetVkey",
                        "method": "GetUrl",
                        "param": {
                            "guid": "1519536863",
                            "songmid": [
                                "003S1hgM2asCye"
                            ],
                            "songtype": [
                                0
                            ],
                            "uin": "2172093349",
                            "loginflag": 1,
                            "platform": "20"
                        }
                    }
                }
                # 修改表单
                # 修改 songMID 和 songmid
                dataDW['req_1']['param']['songMID'] = mid
                dataDW['req_4']['param']['songmid'][0] = mid
                # 修改 songID 和 biz_id
                dataDW['req_1']['param']['songID'] = pid
                dataDW['req_2']['param']['request_list'][0]['biz_id'] = pid
                # 修改albumMid
                dataDW['req_3']['param']['albumMid'] = albumMid
                # 修改guid
                dataDW['req_4']['param']['guid'] = guid()
                dataDW = json.dumps(dataDW, ensure_ascii=False)

                # 获取参数sign
                def signDW():
                    fle = f'{kesPath}\\wordsJS\\sign.js'
                    return execjs.compile(Path(fle).read_text(encoding='utf-8')).call('sign', dataDW)

                params = {
                    "_": round(time.time() * 1000),
                    "sign": signDW(),
                }
                response = requests.post(
                    url='https://u6.y.qq.com/cgi-bin/musics.fcg',
                    headers=headers,
                    cookies=cookies,
                    params=params,
                    data=dataDW
                ).json()
                # 清洗数据
                # 获取歌曲下载链接
                sip = response['req_4']['data']['sip'][0]
                purl = response['req_4']['data']['midurlinfo'][0]['purl']
                dw_link = sip + purl
                # 获取歌曲名字
                m_title = main_info['歌曲']
                # 获取作者
                m_author = main_info['作者']
                # 获取专辑名字
                music_album = main_info['专辑']
                datalist.append(
                    {
                        "m_title": m_title,
                        "m_author": m_author,
                        "DW_link": dw_link,
                        'music_album':music_album,
                    }
                )
                time.sleep(0.4)
            return datalist


        while True:
            print("------------------------------------------------------")
            print("[1] 下载歌曲\n"
                  "[2] 保存Excel信息\n"
                  "[back] 返回\n")
            cce = input("选择:")
            if cce == "back":
                break
            if cce == "1":
                print("正在加载..请等待")
                req_DW = req_DW()
                while True:
                    print("--------------------------------------------------------------------------------")
                    print("[1] 单曲下载\n"
                          "[2] 批量下载\n"
                          "[back] 返回\n")
                    pick = input("选择:")
                    # 用于单曲下载的数据
                    def pick_item():
                        try:
                            sequence = int(input("歌曲序列号:"))
                            if sequence > len(req_DW) or sequence < 1:
                                print("请输入一个有效的序列号")
                            else:
                                m_title = req_DW[sequence - 1]['m_title'].replace('/', "__").replace("\\", " ").replace('?', '__')
                                m_author = str(req_DW[sequence - 1]['m_author']).replace('/', "__").replace("\\", " ").replace('?', '__')
                                m_album = req_DW[sequence - 1]['music_album'].replace('/', "__").replace("\\", " ").replace('?', '__')
                                dw_link = req_DW[sequence - 1]['DW_link']
                                return m_title, m_author,m_album, dw_link
                        except ValueError:
                            print(None)



                    if pick == "1":
                        pick_itemDef = pick_item()
                        m_title = pick_itemDef[0]
                        m_author = pick_itemDef[1]
                        m_album = pick_itemDef[2]
                        dw_link = pick_itemDef[3]
                        # 向音频地址发起请求
                        pickMusic_get = requests.get(url=dw_link).content


                        def StoragePath_item(e):
                            fle = f'{e}\\{m_title}-{m_author}'
                            os.makedirs(fle, exist_ok=True)
                            accele = f'{fle}\\{m_title}-{m_author}'
                            if not Path(f"{accele}.wav").exists():
                                with open(f"{accele}.wav", "wb") as f:
                                    f.write(pickMusic_get)
                            else:
                                with open(f"{accele}__{m_album}.wav", "wb") as f:
                                    f.write(pickMusic_get)
                            print(f"已保存==================路径 {fle}")


                        print("--------------------------------------------------------------------------------")
                        print("[1] 默认路径\n"
                              "[2] 自定义路径")
                        StoragePath = input("选择:")
                        # 默认路径
                        if StoragePath == "1":
                            pathdirP = f'{kesPath}\\歌曲\\单曲下载'
                            StoragePath_item(pathdirP)
                        # 自定义路径
                        if StoragePath == "2":
                            CustomizePath = input("目标路径:")
                            pathdirP = f'{CustomizePath}'
                            StoragePath_item(pathdirP)
                    if pick == "2":
                        def StoragePath2_item(e):
                            print("--------------------------------------------------------------------------------")
                            print("[1] 全部位于同一目录\n"
                                  "[2] 独立包装存储")
                            storage_path = input("选择:")
                            fle1 = f'{e}\\{user_serch}'
                            for i in tqdm(req_DW, desc="正在全速下载", leave=False):
                                m_title = i['m_title'].replace('/', " ").replace("\\", " ").replace('?','-')
                                m_author = i['m_author'].replace('/', " ").replace("\\", " ").replace('?','-')
                                m_album = i['music_album'].replace('/', " ").replace("\\", " ").replace('?','-')
                                m_link = i['DW_link']
                                pickMusic2_get = requests.get(url=m_link).content
                                if storage_path == "1":
                                    os.makedirs(fle1, exist_ok=True)
                                    fdde = f"{fle1}\\{m_title}-{m_author}"
                                    if not Path(f"{fdde}.wav").exists():
                                        with open(f"{fdde}.wav", "wb") as f:
                                            f.write(pickMusic2_get)
                                    else:
                                        with open(f"{fdde}__{m_album}.wav", "wb") as f:
                                            f.write(pickMusic2_get)
                                if storage_path == "2":
                                    fle2 = f'{fle1}\\{m_title}-{m_author}'
                                    os.makedirs(fle2, exist_ok=True)
                                    with open(f"{fle2}\\{m_title}-{m_author}.wav", "wb") as f:
                                        f.write(pickMusic2_get)
                            print(f"已保存==================路径 {fle1}")

                        print("--------------------------------------------------------------------------------")
                        print("[1] 默认路径\n"
                              "[2] 自定义路径")
                        StoragePath2 = input("选择:")
                        # 默认路径
                        if StoragePath2 == "1":
                            pathdirP = f'{kesPath}\\歌曲\\批量下载'
                            StoragePath2_item(pathdirP)
                        # 自定义路径
                        if StoragePath2 == "2":
                            CustomizePath = input("目标路径:")
                            pathdirP = f'{CustomizePath}'
                            StoragePath2_item(pathdirP)
                    if pick == "back":
                        break

            if cce == "2":
                print('敬请期待===================')
    except KeyboardInterrupt:
        print("\n手动退出程序........")
        break