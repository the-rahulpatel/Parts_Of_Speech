
import anthropic
import os

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=os.environ.get("CLAUDE_API"),
)

user_input = input("Enter your input: ")
message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": f"You are now an expert at identifying parts of speech. You are a British grammar master, and all kinds of people come to you irrespective of their proficiency in the English langauge. In the following sentence accurately identify the technical grammar terms for each word in British English:{user_input}"}
    ]
)
print(message.content[0].text)
