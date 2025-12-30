class Codec:
    def __init__(self):
        self.url_map = {}
        self.counter = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        self.counter += 1
        short_key = str(self.counter)
        self.url_map[short_key] = longUrl
        return "http://tinyurl.com/" + short_key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        short_key = shortUrl.split("/")[-1]
        return self.url_map[short_key]
