# importing all the required modules 
from django.http import FileResponse
from django.shortcuts import render, redirect 
import os
from pytube import *

# defining function 
def youtube(request): 
	# checking whether request.method is post or not 
	if request.method == 'POST': 
		path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')
  
		# getting link from frontend 
		link = request.POST['link'] 
		video = YouTube(link) 

		# setting video resolution 
		stream = video.streams.get_lowest_resolution() 
		
		# downloads video 
		stream.download(output_path=path, skip_existing=False)
		
		# returning HTML page 
		return render(request, 'downloader/youtube.html') 
	return render(request, 'downloader/youtube.html')
