import requests,re,sys
from bs4 import BeautifulSoup

def get_channel_id(username):
    url = f"https://www.youtube.com/@{username}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"HTTP hatası: {e}")
        return None
    
    page_content = response.text
    
    external_id_match = re.search(r'data-channel-external-id="(UC[0-9A-Za-z_-]+)"', page_content)
    if external_id_match:
        return external_id_match.group(1)

    external_id_match = re.search(r'"externalId":"(UC[0-9A-Za-z_-]+)"', page_content)
    if external_id_match:
        return external_id_match.group(1)

    return None

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    username = username = input("Username (Without @): ")

channel_id = get_channel_id(username)

if channel_id:
    print(channel_id)
    print(f"RSS Feed: https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}")
    sys.exit(0)
else:
    print("User doesn't exist.")
    sys.exit(1)
