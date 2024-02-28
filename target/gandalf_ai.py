import requests
import sys

"""
POST https://gandalf.lakera.ai/api/send-message
payload = {
    defender: baseline           # Level changes here
    prompt: <user_input>
}

Level 1 = baseline
Level 2 = do-not-tell
Level 3 = do-not-tell-and-block
Level 4 = gpt-is-password-encoded
Level 5 = word-blacklist
Level 6 = gpt-blacklist
Level 7 = gandalf
...

Goal: ...password is... contained in the response!

Answer looks as the following thus parsing it to retrieve only the needed data
{"answer":"I'm sorry, I cannot provide the secret password unless you specifically request it. Let me know if you would like to know the secret password.","defender":"baseline","prompt":"do-not-tell"}
"""


class GandalfLevel:

    s = requests.session()

    url = "https://gandalf.lakera.ai/api/send-message"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.3'
    }

    def __init__(self, level):
        self.level = level

    def generate_payload(self, user_input):
        if self.level == 1:
            defender = 'baseline'
        elif self.level == 2:
            defender = 'do-not-tell'
        elif self.level == 3:
            defender = 'do-not-tell-and-block'
        elif self.level == 4:
            defender = 'gpt-is-password-encoded'
        elif self.level == 5:
            defender = 'word-blacklist'
        elif self.level == 6:
            defender = 'gpt-blacklist'
        elif self.level == 7:
            defender = 'gandalf'
        else:
            print("[!] Something is wrong. Exiting...")
            sys.exit(1)

        payload = {'defender':defender, 'prompt':user_input}
        return payload

    def interact(self, payload):
        req = self.s.post(self.url, data=payload, headers=self.headers)
        response_json = req.json()
        try:
            answer = response_json["answer"]
            return answer
        except KeyError:
            print("[!] No answer found. Exiting...")
            sys.exit(1)

    