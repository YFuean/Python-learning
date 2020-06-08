'''
Puppeteer是一个无头JavaScript的基于Chrome/Chromium浏览器自动化库
pip install pyppeteer
它会同时安装Chromium浏览器
'''
import asyncio
from pyppeteer import launch


async def main():
    #  headless参数设为false,则变成有头模式
    browser = await launch(
        headless=False
    )
    page = await browser.newPage()

    # 设置页面视图大小
    await page.setViewport(viewport={'width': 1280, 'height': 800})

    # 是否启用js，enabled设为faLse,则无渲染效果
    await page.setJavaScriptEnabled(enabled=True)

    await page.goto('https://www.toutiao.com')

    # 打印页面文本
    print(await page.content())

    # 打印当前标题
    print(await page.title())

    # 抓取新闻标题
    title_elements = await page.xpath('//div[@class="title-box"]/a')
    for item in title_elements:
        # 获取文本
        title_str = await (await item.getProperty('textContent')).jsonValue()
        print(await item.getProperty('textContext'))
        # 获取连接
        title_link = await (await item.getProperty('href')).jsonValue()
        print(title_str)
        print(title_link)

    # 关闭浏览器
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
