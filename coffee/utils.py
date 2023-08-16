import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")


def reduce_content(text: str) -> str:
    """Given content return a single haiku only (sometimes the API returns more than one haiku)"""
    lines = text.split('\n')
    return "\n".join((lines[0], lines[1], lines[2]))


def get_haiku() -> str:
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": """
            You are a master haiku writer. 
            Write a haiku about a speciality coffee cafe which is described below. The haiku should be visual and dreamy 
            with occasional scenic or color references. Never mention prices. 
    
            Below:
            perfectly roasted bean
            pretty latte art 
            tasty
            dark
    
            The cafe is described as: This is the best coffee in the area by far. The people are always friendly.
            
            A single 3 line haiku should be returned
            """
                   }],
        temperature=0.7,
    )

    content = chat_completion.choices[0].message.content
    haiku = reduce_content(content)
    return haiku



