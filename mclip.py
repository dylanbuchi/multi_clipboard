import sys
import pyperclip

#constant global variable dictionary LINK
LINKS = {
    'python': 'https://www.python.org/',
    'github': 'https://github.com/',
    'java': 'https://docs.oracle.com/en/java/',
    'youtube': 'https://www.youtube.com/',
    'reddit': 'https://www.reddit.com/',
}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mclip.py [keyphrase] - copy link")

        # a default value copied
        pyperclip.copy("Hellooo")
        sys.exit()

    # first command line arg is the keyphrase
    keyphrase = sys.argv[1]

    if keyphrase in LINKS:
        #copy the value of the key into user copy-paste clip
        pyperclip.copy(LINKS[keyphrase])
        print(f"link for {keyphrase} website copied to clipboard.")
else:
    print(f"There is no link for {keyphrase}")
