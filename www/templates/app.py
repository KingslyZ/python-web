import logging;logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
from datetime import datetime

from aiohttp import web,web_runner


routes = web.RouteTableDef()

@routes.get('/')
def index(request):
    #页面显示内容
    return web.Response(body=b'<h1>Awesome App</h1>', content_type='text/html')

def init():
    # 初始化实例
    app = web.Application()
    # 访问地址
    app.add_routes([web.get('/', index)])
    # 登录信息
    logging.info('server started at http://127.0.0.1:9000...')
    # 执行
    web.run_app(app, host='127.0.0.1', port=9000)


init()