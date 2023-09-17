import webbrowser
from youtubesearchpython import VideosSearch

def func_openSite(url):
    webbrowser.open(url)
def func_sendMail(*args):
    print("TODO")
def func_playSong(song_name):
    try:
        videos_search = VideosSearch(song_name, limit = 1)
        results = videos_search.result()

        # Extract the URL of the first search result
        if results['result']:
            first_result = results['result'][0]
            video_url = "https://www.youtube.com/watch?v=" + first_result['id']
            webbrowser.open(video_url)
        else:
            print("No results found for the song.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")