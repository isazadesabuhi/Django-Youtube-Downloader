from django.shortcuts import render
from pytube import YouTube  # Make sure to install pytube with pip install pytube

def download_video(request):
    context = {}
    if request.method == 'POST':
        video_url = request.POST.get('url', '')
        if video_url:
            yt = YouTube(video_url)
            download_directory = "C:/Users/sabuh/Projects"
            yt.streams.get_highest_resolution().download(output_path=download_directory)
            context['message'] = 'Download completed!'
            context['download_path'] = download_directory
    return render(request, 'downloader/download_form.html', context)
