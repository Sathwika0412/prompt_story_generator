import openai

# Replace with your actual API key
openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_story(prompt):
    few_shot_example = """
    Prompt: A lonely robot on Mars finds a mysterious signal.
    Story: On the desolate plains of Mars, a robot named Mira roamed endlessly. One evening, her sensors detected a strange rhythmic pulse...
    """

    full_prompt = few_shot_example + f"\nPrompt: {prompt}\nStory:"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=full_prompt,
        max_tokens=200,
        temperature=0.8,
        top_p=0.95
    )

    story = response.choices[0].text.strip()
    return story

# Example run
if __name__ == "__main__":
    user_prompt = input("Enter a prompt: ")
    print("\nGenerated Story:\n")
    print(generate_story(user_prompt))
