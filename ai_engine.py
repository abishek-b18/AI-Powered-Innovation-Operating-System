import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_blueprint(idea):

    prompt = f"""
    Generate a startup blueprint for:

    {idea}

    Include:
    1. Problem Statement
    2. Solution
    3. Business Model
    4. Revenue Model
    5. Technical Architecture
    6. Development Roadmap
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response["choices"][0]["message"]["content"]