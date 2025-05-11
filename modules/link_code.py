from urllib.parse import urlparse, parse_qs

class Code:
    def retriever(link):
        try:
            parsed_url = urlparse(url=link)
            if "youtu.be" in parsed_url.netloc:
                return (parsed_url.path.lstrip("/"))
            
            elif "youtube.com" in parsed_url.netloc:
                query = parse_qs(parsed_url.query)
                return (query["v"][0]) if "v" in query else None
    
        except Exception as e:
            print("Exception Parsing URL: ", e)
            return None