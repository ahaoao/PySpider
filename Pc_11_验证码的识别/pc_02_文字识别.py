import os
from aip import AipOcr
import keyboard
from PIL import ImageGrab
from time import sleep


def get_reuslt(img_name):
    APP_ID = '17298958'
    API_KEY = '73InuoZ46w3UhNfaP6ekfHA8'
    SECRET_KEY = 'tooFkOGh2M4MoEyvKlwWGxZCdsPbaU6G'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    """ 读取图片 """
    with open(img_name, 'rb') as fp:
        image = fp.read()
    """ 如果有可选参数 """
    options = {}
    options["detect_direction"] = "true"
    options["probability"] = "false"
    """ 带参数调用通用文字识别（高精度版） """
    client = client.basicAccurate(image, options)
    for i in client['words_result']:
        reuslt = i['words']
        print(reuslt+'\t')
        with open(img_name+'.txt', 'a', encoding='utf-8') as f:
            f.write(reuslt+'\n')
    print("文本已经保存本地")


def jietu():
    while 1:
        keyboard.wait('f12', '')
        keyboard.wait('ctrl+c')
        sleep(0.2)
        image = ImageGrab.grabclipboard()
        # 从剪贴版获取图片
        image.save('截图.jpg')
        for filename in os.listdir(r"./"):
            if (filename.endswith('.jpg')) or (filename.endswith('.png')) or (filename.endswith('.bmp')):
                get_reuslt(filename)
        print('请继续截图....')


def main():
    for filename in os.listdir(r"./"):
        if (filename.endswith('.jpg')) or (filename.endswith('.png')) or (filename.endswith('.bmp')):
            get_reuslt(filename)


if __name__ == '__main__':
    print('********'*2+'请选择图片识别方式'+'********'*2+'\n')
    print('截屏识别填1，图片识别填2(推荐使用方式2)')
    pd = input('请输入你的选择：')
    print('********' * 2 + '*********' * 2 + '********' * 2 + '\n')
    if pd == '2':
        print('***************请将图片放置本目录下***************')
        a = input("我已将图片放好？  （y/n）：")
        if a == 'y':
            main()
        else:
            pass
    else:
        print('只支持快捷键F1截屏，需要按 Ctrl+c 将图片存到剪贴板...')
        print('请开始截图.......')
        jietu()