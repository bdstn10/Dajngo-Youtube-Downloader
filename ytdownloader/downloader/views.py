from io import BytesIO
from django.http import FileResponse
from django.views.generic import View
from pytube import YouTube
from django.shortcuts import render,redirect

class home(View):
    def __init__(self,url=None):
        self.url = url
    def get(self,request):
        return render(request,'downloader/youtube.html')    
    def post(self,request):
        # for fetching the video
        if request.POST.get('fetch-vid'):
            self.url = request.POST.get('given_url')
            video = YouTube(self.url)
            vidTitle,vidThumbnail = video.title,video.thumbnail_url
            qual,stream = [],[]
            for vid in video.streams.filter(progressive=True):
                qual.append(vid.resolution)
                stream.append(vid)
            context = {'vidTitle':vidTitle,'vidThumbnail':vidThumbnail,
                        'qual':qual,'stream':stream,
                        'url':self.url}
            return render(request,'downloader/youtube.html',context)

        # for downloading the video
        elif request.POST.get('download-vid'):
            self.url = request.POST.get('given_url')
            video = YouTube(self.url)
            stream = [x for x in video.streams.filter(progressive=True)]
            video_qual = video.streams[int(request.POST.get('download-vid')) - 1]
            
            response_file = BytesIO()
            video_qual.stream_to_buffer(response_file)
            response_file.seek(0)
            
            response = FileResponse(response_file, as_attachment=True, filename=video_qual.default_filename)
            # response['Content-Disposition'] = f'attachment; filename={video_qual.default_filename}'
            return response
            

        return render(request,'downloader/youtube.html')
