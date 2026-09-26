import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_test_cases(requirement):
    prompt = f"""
You are a senior QA engineer.

Generate test cases for this requirement:

{requirement}

Include:
- Positive test cases
- Negative test cases
- Boundary test cases
- Edge cases
"""

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt,
    )

    return response.output_text


if __name__ == "__main__":
    requirement = "A customer can transfer up to $5,000 per day."

    result = generate_test_cases(requirement)

    print(result)