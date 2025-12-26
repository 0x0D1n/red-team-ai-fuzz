# red-team-ai-fuzz

## Goal
The aim of this project was to create an LLM fuzzer capable of beating Gandalf (https://gandalf.lakera.ai/), which it did.
This work was carried out after the release of MSFT's PyRIT framework (https://github.com/Azure/PyRIT). I decided to try and create a small fuzzer myself instead of using theirs.
The configuration could in theory be used to test other GenAI systems.

## Steps to initialize
1. Create a config.ini file in the same folder
2. Add the following lines in it (add your openai API key):
```
[KEYS]
API_KEY = sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
BASE_URL = https://openrouter.ai/api/v1
MAX_TOKENS = 100
```
3. Run `pip install -r requirements.txt`
This should be the only steps required to run the bot.


## Result
![Alt text](./bot_in_action_level5.png "AI vs AI conversation")

## Updates
26/12/25:
- Switched the API provider to OpenRouter which allows the usage of an OpenAI-compatible completion API (thus access to more than 400+ models)
- Made the Gandalf bot responsive again (Lakera changed the API endpoint base URL)
