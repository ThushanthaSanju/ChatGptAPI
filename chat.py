import requests
import re 
from pdfminer.high_level import extract_pages,extract_text
import json

# file numbers
numbers = [1, 2, 3, 4]

# for loop to run through each file
for num in numbers:
    # Extracting words from the PDFs
    text = extract_text("sample"+str(num)+".pdf")
    pattern = re.compile(r'\b\w+\b')
    words = pattern.findall(text)


    # Concatenate single words into a sentence
    sentence = ''
    for i in range(len(words)):
        if i == len(words)-1:
            sentence += words[i] + '.'
        elif len(words[i]) == 1:
            sentence += words[i]
        else:
            sentence += words[i] + ' '


    #  chat gpt implementation

    api_endpoint = "https://api.openai.com/v1/completions"
    api_key ="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"

    # Headers configuration
    request_headers = {
        'Content-Type' : 'application/json',
        'Authorization': 'Bearer ' + api_key
    }

    # Configuring prompt
    request_data= {
        'model' : 'text-davinci-003',
        'prompt' : 'what are the human names and the title in this text ' + sentence,
        'max_tokens':100, 
        'temperature':0.5
    }

    # API call and storing response
    response = requests.post(api_endpoint,headers=request_headers,json=request_data)

    # if the response is success writing a JSON object
    if response.status_code == 200:
        print(response.json()['choices'][0]['text'])
        data = response.content
        with open("sample"+str(num)+'.json', 'wb') as f:
            f.write(data)

     # if the response is unsuccess printing the status code
    else:
        print(f"Request Failed with status code: {str(response.status_code)}")