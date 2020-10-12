import re
import string


class CleanData:
    def de_emojify(self, tweet):
        """Remove emoticons from given text"""
        regrex_pattern = re.compile(
            pattern="["
            "\U0001F600-\U0001F64F"  # emoticons
            "\U0001F300-\U0001F5FF"  # symbols & pictographs
            "\U0001F680-\U0001F6FF"  # transport & map symbols
            "\U0001F1E0-\U0001F1FF"  # flags (iOS)
            "\U00002500-\U00002BEF"  # chinese char
            "\U00002702-\U000027B0"
            "\U00002702-\U000027B0"
            "\U000024C2-\U0001F251"
            "\U0001f926-\U0001f937"
            "\U00010000-\U0010ffff"
            "\u2640-\u2642"
            "\u2600-\u2B55"
            "\u200d"
            "\u23cf"
            "\u23e9"
            "\u231a"
            "\ufe0f"  # dingbats
            "\u3030"
            "]+",
            flags=re.UNICODE,
        )
        return regrex_pattern.sub(r"", tweet)

    def remove_punctuation(self, tweet):
        """Remove links and other punctuation from text"""
        tweet = tweet.replace("\n", "")
        tweet = tweet.replace("\t", "")
        re.sub(r"http\S+", "", tweet)  # removes links

        translator = str.maketrans("", "", string.punctuation)
        return tweet.lower().translate(translator)
