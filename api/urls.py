from api.controllers import HomeView, download_video, get_video_info


def add_routes(app):
    app.add_url_rule('/', view_func=HomeView.as_view('home'))
    app.add_url_rule('/api/download', view_func=get_video_info, methods=['GET'])
    app.add_url_rule('/api/download/<resolution>', view_func=download_video, methods=['POST'])