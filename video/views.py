from django.shortcuts import render
from video.api import title
# Create your views here.

def index(req):
    url="http://www.9558.tv"
    html_text=title.get_content(url=url)
    url_list=title.get_data(html_text)
    for item in range(0,len(url_list)):
        print(url_list[item])
        url_list[item].append(title.get_video(url_list[item][0]))
    print(url_list)
    return render(req,'index_video.html',{'list':url_list})