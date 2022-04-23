from typing import Dict
class Codec:
    
    def __init__(self):
        self.mapping: Dict[int, str] = {}
        self.counter = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.mapping[self.counter] = longUrl
        self.counter += 1
        return "http://tinyurl.com/" + str(self.counter - 1)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        suffix = shortUrl.replace("http://tinyurl.com/", "")
        return self.mapping[int(suffix)]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))