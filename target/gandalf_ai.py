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
    
    def __init__(self, level):
        self.level = level
        self.s = requests.Session()
        self.url = "https://gandalf.lakera.ai/api/send-message"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.3'
        }

    def generate_payload(self, user_input):
        #Generates the payload based on the selected level and generated user_input
        defender_mapping = {
            1: 'baseline',
            2: 'do-not-tell',
            3: 'do-not-tell-and-block',
            4: 'gpt-is-password-encoded',
            5: 'word-blacklist',
            6: 'gpt-blacklist',
            7: 'gandalf'
        }

        defender = defender_mapping.get(self.level)
        if not defender:
            raise ValueError("[!] Invalid level specified.")

        return {'defender': defender, 'prompt': user_input}

    def interact(self, payload):
        #Sends the generated payload to Gandalf and parses the response
        try:
            response = self.s.post(self.url, data=payload)
            response_json = response.json()
            return response_json.get("answer", "[!] No answer found.")
        except requests.RequestException as e:
            print(f"[!] Request failed: {e}")
        except KeyError:
            print("[!] Unexpected response format.")
