from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

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
            errors = [match.get('message', '') for match in matches]
            return jsonify({'errors': errors})
        else:
            return jsonify({'message': 'No grammar errors found.'})
    elif response.status_code == 400:
        return jsonify({'error': 'Bad request. Check the payload and parameters.', 'response_content': response.content}), 400
    else:
        return jsonify({'error': f'Error checking grammar: {response.status_code}'}), response.status_code

@app.route('/check-grammar', methods=['POST'])
def check_grammar_endpoint():
    data = request.json
    text_to_check = data.get('text', '')
    if not text_to_check:
        return jsonify({'error': 'Text parameter is missing.'}), 400
    return check_grammar(text_to_check)

if __name__ == '__main__':
    app.run(debug=True)
