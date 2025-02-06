from litellm import completion
import os


os.environ["GEMINI_API_KEY"] = "" 



def gemini():
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[{ "content": "Hello, What are you working on right now?","role": "user"}]
    )

    print(response['choices'][0]['message']['content'])
