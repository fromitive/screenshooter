import os
from django.shortcuts import render
from django.conf import settings
from .screenshoter import Screenshoter
from .models import QRinfo
from .virt.scan_url import scan_url
IMAGE_DIR = 'images'
def main_page(request):
    return render(request,'app/main_page.html',{})

def get_screenshot(request):
    print("-"*10,"result","-"*10)
    print(request.POST)       
    #need to URL validation
    qrinfo = QRinfo.objects
    if request.method == 'POST' and 'url' in request.POST:
        url = request.POST.get('url','')
        if url is not None and url != '':
            scan_result = scan_url(url)
            if not scan_result['positives']:
                try:
                    img_path = qrinfo.get(url=url).img_path
                    return render(request,'app/screenshot.html',{'image':img_path,'malscan':scan_result})
                except Exception as e: 
                    print(e)
                    dir_path = 'app/static/images' 
                    srcshot = Screenshoter(url,dir_path)
                    img_name = srcshot.shot()
                    img_path = os.path.join(IMAGE_DIR,img_name) 
                    qrinfo.create(url=url,img_path=img_path)
                    return render(request,'app/screenshot.html',{'image':img_path,'malscan':scan_result})
    else:
        return render(request,'app/screenshot.html',{})
