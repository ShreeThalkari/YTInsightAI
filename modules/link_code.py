from urllib.parse import urlparse, parse_qs


class Code:
    @staticmethod
    def retrieve(link: str) -> str | None:
        """
        Extracts the YouTube video ID from the URL.
        Supports both youtu.be and youtube.com formats.
        """
        try:
            parsed_url = urlparse(link)
            if "youtu.be" in parsed_url.netloc:
                return parsed_url.path.lstrip("/")
            elif "youtube.com" in parsed_url.netloc:
                query = parse_qs(parsed_url.query)
                return query.get("v", [None])[0]
            else:
                return None
        except Exception as e:
            print(f"Exception parsing URL: {e}")
            return None
