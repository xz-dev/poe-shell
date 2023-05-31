# poe-shell.py 

This is a shell tool for accessing poe.com. (NO Waiting Error!)  
It wraps almost all webpage functions on poe.com through [ading2210/poe-api](https://github.com/ading2210/poe-api).  

## Installation

```bash
pip3 install poe-api
```

## Usage

### Basic

```bash
POE_TOKEN=<YOUR_POE_TOKEN> ./poe-shell.py <function_name> <function_args>
``` 

Before using, you need to get an API token from poe.com and save it to the POE_TOKEN environment variable.  

Then you can call any function defined in poe-api by passing in the function name and arguments. For example:

```bash
POE_TOKEN=xxxxxxx ./poe-shell.py bot_names | jq . 
POE_TOKEN=xxxxxxx ./poe-shell.py send_message capybara "hello 你好" | jq -r '.text_new' | tr -d '\n' 
``` 

For specific functions and arguments, please refer to [ading2210/poe-api](https://github.com/ading2210/poe-api). 

### Plus

You **also can** use it to do some hard thing by poe-api or by website

```bash
# Clean all bot message
for bot in $(./poe-shell.py bot_names | jq -r 'keys[]'); do echo $bot; ./poe-shell.py purge_conversation "$bot"; done
```

### UI mode

```bash
🚀./poe-shell.py send_message capybara {input} # support multi line input, Ctrl-D to break input
(.venv) UI mode enabled
function parameters: ['chatbot', 'message', 'with_chat_break', 'timeout']
message: Hello
message: 你好呀
{'id': 'TWVzc2FnZTo5OTA2MDg0MzI=', 'messageId': 990608432, 'creationTime': 1685469024963210, 'state': 'incomplete', 'text': 'Hello! How can I assist you today?', 'author': 'capybara', 'linkifiedText': 'Hello! How can I assist you today?', 'suggestedReplies': [], 'vote': None, 'voteReason': None, 'text_new': '?'}
```

### Bash command helpper

``` bash
$ ./helpper/poe-botname.sh Sage
capybara
# Clean Sage message
$ ./poe-shell.py purge_conversation $(./helper/poe-botname.sh Sage)
```

## Feedback   

If you encounter any issues or have feature requests, feel free to file an issue or pull request. 

## End

All code from poe's gpt4 self, I just review all code and check it running.  
Thanks all dev for AI and about AI :)  

# More Toy

[poe_sidebar_robots_remover](https://github.com/xz-dev/poe_sidebar_robots_remover): Remove Poe.com useless Robots from Sidebar  
More intresting project check in my [homepage😄](https://github.com/xz-dev)  
