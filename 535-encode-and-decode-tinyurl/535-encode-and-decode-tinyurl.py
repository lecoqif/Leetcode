from typing import Dict
class Codec:
    
    def __init__(self):
        self.mapping: Dict[str, str] = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        shortUrlSuffix = str(hash(longUrl))
        self.mapping[shortUrlSuffix] = longUrl
        return "http://tinyurl.com/" + shortUrlSuffix

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        suffix = shortUrl.replace("http://tinyurl.com/", "")
        return self.mapping[suffix]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))