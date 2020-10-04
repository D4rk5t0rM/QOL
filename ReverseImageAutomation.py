import urllib
import webbrowser
import pyperclip
import time

def main():
    print("Please provide a link to an image - press enter to read from clipboard:   ")
    try:
        link = urllib.parse.quote(input())
        if link == '':
            link = pyperclip.paste()
        link = link.replace('/','%2F')
    except Exception as e:
        print("crash with reading the link. \nErrorcode: "+e)
    #open a webbrowser on the right page:
    webbrowser.open('https://www.bing.com/images/search?view=detailv2&iss=sbi&FORM=SBIHMP&sbisrc=UrlPaste&q=imgurl:'+link)
    time.sleep(0.2)
    webbrowser.open('https://yandex.com/images/search?url='+link+'&rpt=imageview&uinfo=sw-1920-sh-1080-ww-1920-wh-966-pd-1-wp-16x9_1920x1080&source-serpid=mXeJHg0PCopDf_AKx1-i4A')
    time.sleep(0.2)
    webbrowser.open('https://images.google.com/searchbyimage?image_url='+link)
main()