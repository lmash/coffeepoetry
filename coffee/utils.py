from dotenv import load_dotenv
import os
import openai


# Load your API key from an environment variable or secret management service
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def reduce_content(text: str) -> str:
    """Given content return a single haiku only (sometimes the API returns more than one haiku)"""
    lines = text.split('\n')
    return "\n".join((lines[0], lines[1], lines[2]))


def get_haiku(adjectives=None, cafe_description=None) -> str:
    if not adjectives:
        adjectives = """
                    perfectly roasted bean
                    pretty latte art 
                    tasty
                    dark
        """

    if not cafe_description:
        cafe_description = """This is the best coffee in the area by far. The people are always friendly."""

    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"""
            You are a master haiku writer. 
            Write a haiku about a speciality coffee cafe which is described below. The haiku should be visual and dreamy 
            with occasional scenic or color references. Never mention prices. 
    
            Below: {adjectives}

            The cafe is described as: {cafe_description}
            
            A single 3 line haiku should be returned
            """
                   }],
        temperature=0.7,
    )

    content = chat_completion.choices[0].message.content
    haiku = reduce_content(content)
    return haiku


poem = get_haiku()
print(poem)
