# coding=utf-8

import urllib
import hashlib
import time

import requests

from weixin_helper.helper import HelperMixin


class WeixinError(Exception):
    pass


class WeixinMpHelper(HelperMixin, object):
    """weixin 公众号常用操作"""

    _WEIXIN_ACCESSTOKEN_URL = "https://api.weixin.qq.com/cgi-bin/token?"
    _WEIXIN_JSAPI_TICKET_URL = "https://api.weixin.qq.com/cgi-bin/ticket/getticket?"

    def __init__(self, appid="", secret=""):
        """根据 weixin 文档中的描述，鉴于 api 调用次数每日限制，
        因此获取 access_token 以及 jsapi_ticket 都需要进行缓存
        默认的失效时间是 7200 秒"""

        # 由于者两个参数将导致 http 访问，因此进行了类型检查
        # @XXX 类型检查
        assert appid != "" and secret != ""

        self.appid = appid
        self.secret = secret

    def get_access_token(self):
        params = {"grant_type": "client_credential",
                  "appid": self.appid,
                  "secret": self.secret}

        res = requests.get("".join([self._WEIXIN_ACCESSTOKEN_URL, urllib.urlencode(params)]))
        res_info = res.json()

        access_token = res_info.get("access_token", "")
        if access_token == "":
            raise WeixinError("get access_token error: %s", res.text)

        return access_token

    def get_jsapi_ticket(self, access_token=""):
        assert access_token != ""

        params = {"access_token": access_token,
                  "type": "jsapi"}

        res = requests.get("".join([self._WEIXIN_JSAPI_TICKET_URL, urllib.urlencode(params)]))
        res_info = res.json()

        ticket = res_info.get("ticket", "")
        if ticket == "":
            raise WeixinError("get ticket error: %s", res.text)

        return ticket

    def get_js_config(self, url="", debug=False, apis=[]):
        """获取 js 验证所需的 config 信息"""

        access_token = self.get_access_token()
        jsapi_ticket = self.get_jsapi_ticket(access_token=access_token)

        noncestr = self.random_str()
        timestamp = int(time.time())
        url = url
        sign = self.build_sign({"noncestr": noncestr,
                                "jsapi_ticket": jsapi_ticket,
                                "timestamp": timestamp,
                                "url": url})

        return {"debug": debug,
                "appId": self.appid,
                "timestamp": timestamp,
                "nonceStr": noncestr,
                "signature": sign,
                "jsApiList": apis}

def main():
    pass

if __name__ == "__main__":
    main()


