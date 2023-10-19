import pyperclip
import time  

def format_maskedlink(text, url):
    if url.startswith("https://") or url.startswith("http://"):
        return f"[{text}]({url})"
    else:
        return f"[{text}](https://{url})"
    
def format_timestamp(number, suffix , ago_later):

    # Convert the suffix to a number of seconds.
    seconds = int(number)
    if suffix == "min":
        seconds *= 60
    elif suffix == "h":
        seconds *= 3600
    elif suffix == "d":
        seconds *= 86400
    elif suffix == "mo":
        seconds *= 2628000
    else:
        seconds *= 1

    # Calculate the Unix timestamp.
    if ago_later == "ago" or ago_later == "before":
        unix_timestamp = time.time() - seconds
    else:
        unix_timestamp = time.time() + seconds
    return f"<t:{int(unix_timestamp)}:R>"

def main():
    commands = [
        "ml",
        "ts",
        ]

    while True:
        clipboard_text = pyperclip.paste()
        # Remove the command from the clipboard text    
        for command in commands:
            if clipboard_text.startswith(command):        
                stripped_text = clipboard_text[len(command):].strip()            
                parts = stripped_text.split()

                if command == commands[0]: # ml
                    if len(parts) >= 2:
                        text = " ".join(parts[:-1])
                        url = parts[-1]
                        formatted_syntax = format_maskedlink(text, url)
                        pyperclip.copy(formatted_syntax)

                elif command == commands[1]: # ts
                    if len(parts) == 3:
                        number, suffix, ago_later = parts
                        formatted_syntax = format_timestamp(number, suffix, ago_later)
                        pyperclip.copy(formatted_syntax)

                print(f"FormaTom: {formatted_syntax}")

            time.sleep(1)

if __name__ == "__main__":
    main()