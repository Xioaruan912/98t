import requests
import re
from  loguru  import logger
def get_target_url():
    baseurl = 'http://sehuatang.com/'  
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    }
    
    response = requests.get(baseurl, headers=headers, timeout=10)
    response.raise_for_status()
    html = response.text

    pattern = r'mappings\.set\("sehuatang\.com",\s*"(https?://[^"]+)"\)'
    match = re.search(pattern, html)
    

    url = match.group(1)
    return url
