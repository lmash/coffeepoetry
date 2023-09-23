from dotenv import load_dotenv
import openai
import os


# Load your API key from an environment variable or secret management service
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def reduce_content(text: str) -> str:
    """Given content return a single haiku only (sometimes the API returns more than one haiku)"""
    lines = text.split('\n')
    return "\n".join((lines[0], lines[1], lines[2]))


def get_haiku(cafe: str, coffee: str) -> str:
    """
        AI call to generate a haiku based on cafe and coffee descriptions provided
        Returns haiku
    """
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"""
            You are a master haiku writer. 
            Write a haiku about a speciality coffee cafe which is described below. 
            The haiku can have occasional dreamy, scenic or color references. Never mention prices. 

            Below: {coffee}

            The cafe is described as: {cafe}

            A single 3 line haiku should be returned
            """
                   }],
        temperature=0.7,
    )

    content = chat_completion.choices[0].message.content
    haiku = reduce_content(content)
    return haiku
