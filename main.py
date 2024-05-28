import requests

def check_grammar(text):
    url = 'https://api.languagetool.org/v2/check'
    payload = {
        'text': text,
        'language': 'en-US'
    }
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        data = response.json()
        matches = data.get('matches', [])
        if matches:
            for match in matches:
                message = match.get('message', '')
                print(f"Grammar error: {message}")
        else:
            print("No grammar errors found.")
    elif response.status_code == 400:
        print("Bad request. Check the payload and parameters.")
        print("Response content:", response.content)
    else:
        print(f"Error checking grammar: {response.status_code}")

def main():
    text_to_check = input("Enter the text you want to check for grammar errors: ")
    check_grammar(text_to_check)  # Pass the input text to the function

if __name__ == "__main__":
    main()
