# coding=utf-8

import unittest

from weixin_helper.weixin_mp import WeixinMpHelper, WeixinError

# 测试帐号
appid = "wx8c10cb0ddc4ff104"
appsecret = "755e311059118cccc0752ed8ebc61e6b"

class TestWeixinHelper(unittest.TestCase):

    def test_get_access_token_ok(self):
        weixinMpHelper = WeixinMpHelper(appid=appid, secret=appsecret)
        access_token = weixinMpHelper.get_access_token()
        self.assertTrue(access_token != "")

    def test_get_access_token_fail(self):
        """没有正确的设置参数的情况会触发 AssertionError"""

        with self.assertRaises(AssertionError):
            weixinMpHelper = WeixinMpHelper(appid=appid, secret="")

    def test_get_jsapi_ticket_ok(self):
        weixinMpHelper = WeixinMpHelper(appid=appid, secret=appsecret)
        access_token = weixinMpHelper.get_access_token()
        jsapi_ticket = weixinMpHelper.get_access_token()
        self.assertTrue(jsapi_ticket != "")

    def test_get_js_config(self):
        weixinMpHelper = WeixinMpHelper(appid=appid, secret=appsecret)
        config = weixinMpHelper.get_js_config()

        print config
        self.assertTrue("appId" in config)

if __name__ == "__main__":
    unittest.main()


