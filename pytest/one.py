import json

import requests

class one:
    def gettest(self):
        url = 'https://tieba.baidu.com/im/pcmsg/query/getAllUnread'

        params1 = '_=1644324708618'

        url1 = 'https://www.baidu.com'
        header1 = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
            }

        cookie = 'bdshare_firstime=1552880662570; PSTM=1596004211; BIDUPSID=DB0D8129622A8183B1FEE4655D157A94; rpln_guide=1; BDUSS=ldVNmdwaVJOTm5EaXVaUWhZbXNiMS12czc0cWgxMU5uRnRBQ0tRMi1FRVFGWTVnSVFBQUFBJCQAAAAAAAAAAAEAAABX~YGJwsDOpM~-2LwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABCIZmAQiGZgb; BDUSS_BFESS=ldVNmdwaVJOTm5EaXVaUWhZbXNiMS12czc0cWgxMU5uRnRBQ0tRMi1FRVFGWTVnSVFBQUFBJCQAAAAAAAAAAAEAAABX~YGJwsDOpM~-2LwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABCIZmAQiGZgb; __yjs_duid=1_1ec665bfcb7d683a4242adbe5a92597a1619320295547; BAIDUID=20BC9CB7691B1965CD648C93E5CC6565:FG=1; BCLID_BFESS=9936884638439507173; BDSFRCVID_BFESS=FmKOJeC62AV1eGJHl52ybV4Kso19DUvTH6aoju6sZLX8ZmQZb4yREG0PMx8g0Ku-S2MAogKK0eOTHkCF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tRAOoCK-JKvbeJrc5DTD-tFO5eT22-us3Dji2hcH0KLKEfLlbfJky-70DlraLj3i-K8DVlbGbfb1MRjvMR_-KpITWa7z2lozKJn8bq5TtUJYJKnTDMRhqqJXXtQyKMnitIT9-pno0hQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02eCKu-n5jHjc3DNbP; BAIDUID_BFESS=20BC9CB7691B1965CD648C93E5CC6565:FG=1; PSINO=3; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; RT="z=1&dm=baidu.com&si=em0fw80uu&ss=kze3ytqf&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ul=27b&hd=283"; BDRCVFR[S4-dAuiWMmn]=I67x6TjHwwYf0; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; H_PS_PSSID=35105_31660_35774_34584_35490_35801_35797_26350_35765_35745; BA_HECTOR=2g85008l85802h2hiu1h04pq90q; STOKEN=0047bdbcd23b335739954e6996d1b46a86579d614f4ad0385960092c1dc352e2; 2306997591_FRSVideoUploadTip=1; video_bubble2306997591=1; BAIDU_WISE_UID=wapp_1644324690515_631; USER_JUMP=-1; st_key_id=17; ab_sr=1.0.1_NmNhYWUzYmM2NDFiZDdmZDgxNDgzMDczOTQ0YWZhYTQ3OGRhY2FjMmUwOTRlZGZmNTQzZGRlYWM1ZjM4MzQ1MzlhMTYwNTQzZGI4ZjBlZGEwYTEwYWFhZDMzZWZiYmFlNjBiM2I0NjFkOGVmZmU3MTY5ZjY0ZTY1OGRkMjBhYWM5ODcyNmY1MmRjZDI5ZDY1NzY3MDk3M2I4OWMxMGE4N2ZiODEwZTZkNGQ2NTA2ZTA3YjVkY2YzOTg1MzMxODY3; st_data=c61d3fbe9e6000f7557550e090cd913f239b3ade724ea0c861aee2aaaa0f47248b8765f00ddd4a8cf73d643a59820fda2f46eb0e68fc505c415b425c7044e0b4b108b4167829b14337430fa8a146b966d7139809678f34b3e7499f09050f5775; st_sign=bab10025; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1644324690,1644324697,1644324707; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1644324707'
        cookie_dict = {i.split("=")[0]: i.split("=")[-1] for i in cookie.split("; ")}

        re = requests.get(url, params=params1, headers=header1,cookies=cookie_dict, verify=False)
        print(re.json())

        return re.json()

    def posttest(self):
        url = 'https://test-api.onemicroworld.com/users/login'

        body =json.dumps({
        "mobile":"18221981212",
        "password":"123456",
        "device":"android",
        "language":"ch",
        "area_code":"+86",
        "device_no":"test",
        "phone_type":"9500",
        "system":"28",
        "idfa":"test"
        })
        re = requests.post(url, data=body, headers=None, verify=False)
        print(re.json())

if __name__ == '__main__':
   one().gettest()
   #  one().posttest()


