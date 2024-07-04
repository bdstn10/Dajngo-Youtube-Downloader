# importing all the required modules 
from io import BytesIO
from django.http import FileResponse
from django.shortcuts import render, redirect 
import os
from pytube import *
import tempfile

# defining function 
def youtube(request): 
	# checking whether request.method is post or not 
	if request.method == 'POST': 
		# getting link from frontend 
		link = request.POST['link'] 
		video = YouTube(link) 

		# setting video resolution 
		stream = video.streams.get_lowest_resolution() 
		
		# write media stream to buffer
		response_file = BytesIO()
		stream.stream_to_buffer(response_file)
		response_file.seek(0)
  
		# Create FileResponse with the writed buffer
		response = FileResponse(response_file, as_attachment=True)
		response['Content-Disposition'] = f'attachment; filename={stream.default_filename}'
		return response
	return render(request, 'downloader/youtube.html')
