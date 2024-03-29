import os
from flask import render_template, request, jsonify
from flask.views import View
from pytube import YouTube

from utils import get_informacao_video


class HomeView(View):
    def dispatch_request(self):
        return render_template('html/index.html')

def get_video_info():
    video_url = request.args.get('video_url')
    if video_url:
        try:
            resolutions, thumbnail, title = get_informacao_video(video_url)
            return jsonify({'success': True, 'resolutions': resolutions, 'thumbnail': thumbnail, 'title': title})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})
    else: 
        return jsonify({'success': False, 'error': 'URL inválida.'})




def download_video(resolution):
    video_url = request.json['video_url']
    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(res=resolution, progressive=True).first()
        if stream:
            user_download_dir = os.path.join(os.getenv('USERPROFILE'), 'Downloads')
            stream.download(user_download_dir)
            return jsonify({'success': True, 'message': 'Vídeo baixado com sucesso!'})
        else:
            return jsonify({'success': False, 'error': 'Resolução inválida ou não disponível.'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})
