# poe-shell.py 

This is a shell tool for accessing poe.com. It wraps almost all webpage functions on poe.com through [ading2210/poe-api](https://github.com/ading2210/poe-api).

## Installation

```bash
pip3 install poe-api
```

## Usage

```bash
POE_TOKEN=<YOUR_POE_TOKEN> ./poe-shell.py <function_name> <function_args>
``` 

Before using, you need to get an API token from poe.com and save it to the POE_TOKEN environment variable.   

Then you can call any function defined in poe-api by passing in the function name and arguments. For example:

```bash
POE_TOKEN=xxxxxxx ./poe-shell.py bot_names 
POE_TOKEN=xxxxxxx ./poe-shell.py send_message capybara 'hello' 
```

## Supported Features   

poe-shell.py supports all functions defined in poe-api, including:  

- Get league information  
- Get character information  
- Get item information  
- Get skill tree information  
- And more...   

For specific functions and arguments, please refer to [ading2210/poe-api](https://github.com/ading2210/poe-api).

## Feedback   

If you encounter any issues or have feature requests, feel free to file an issue or pull request. 

