from urllib import request
if __name__ =="__main__":
    url = "https://mail.qq.com/cgi-bin/frame_html?sid=ERQGhDuJONylSz9i&r=020c8cd45bac595c463f4eb6c0a11fa0"
    headers = {"Cookie":"pgv_pvi=6580217856; RK=8kTNpE3oQF; tvfe_boss_uuid=7f83a6ce603bc832; _ga=amp-GX-h9bWaxSTilVGX2x68ag; pac_uid=1_1961148165; o_cookie=1961148165; pgv_pvid=2245595246; newpt=2; pgv_si=s3592327168; ptui_loginuin=1961148165; ptisp=cnc; ptcz=13fd92660ec7aac3efe6d7b731e919efe54cafb385778f45dbac55b83c24f957; uin=o1961148165; skey=@IWFuACAq9; p_uin=o1961148165; pt4_token=hylBvHHaQt-DDee1R401ZHlhIIv0Bo2yS8-slLV52Zg_; p_skey=nC44SPmWab1ZMKrLh2M49b635hBDVGy9zj2G8DAa5IE_; wimrefreshrun=0&; qm_logintype=qq; qm_flag=0; qqmail_alias=1961148165@qq.com; sid=1961148165&ff41e014acd8c61b2dbed07bd2c37103,qbkM0NFNQbVdhYjFaTUtyTGgyTTQ5YjYzNWhCRFZHeTl6ajJHOERBYTVJRV8.; qm_username=1961148165; qm_domain=https://mail.qq.com; qm_ptsk=1961148165&@IWFuACAq9; foxacc=1961148165&0; ssl_edition=sail.qq.com; edition=mail.qq.com; qm_loginfrom=1961148165&wpt; username=1961148165&1961148165; new_mail_num=1961148165&327; webp=1; CCSHOW=000000"}
    req = request.Request(url,headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode("gbk")
    with open ("rsp.html","w") as f:
         f.write(html)
