'''
Copyright (c) <2012> Tarek Galal <tare2.galal@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction, including without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR
A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from yowsup.common.http.warequest import WARequest
from yowsup.common.http.waresponseparser import JSONResponseParser


class WARegRequest(WARequest):

    def __init__(self, config, code):
        """
        :param config:
        :type config: yowsup.config.vx.config.Config
        :param code:
        :type code: str
        """
        super(WARegRequest,self).__init__(config)

        if config.id is None:
            raise ValueError("config.id is not set.")

        self.addParam("code", code)

        self.url = "v.whatsapp.net/v2/register"

        self.pvars = ["status", "login", "type", "edge_routing_info", "chat_dns_domain"
                      "reason","retry_after"]

        self.setParser(JSONResponseParser())
