# coding=utf-8

import hashlib
import urllib
from random import Random

class HelperMixin(object):

    def random_str(self, randomlength=32):

        str = ""
        chars = "abcdefghijklmnopqrstuvwxyz0123456789"
        length = len(chars) - 1
        random = Random()

        for i in range(randomlength):
            str += chars[random.randint(0, length)]

        return str

    def build_sign(self, params, hash="sha1"):

        filter = params.keys()
        filter.sort()

        joined_string = "".join(["%s=%s" % (key, params[key])
                                  for key in filter
                                  # filter sign
                                  if params[key] != "" and key != "sign"])

        sign = hashlib.sha1(joined_string).hexdigest()

        return sign


