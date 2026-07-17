import ollama


def ask_ai(prompt):
    """
    Send a prompt to the local AI model.
    """

    response = ollama.chat(
        model="llama3.1:8b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


if __name__ == "__main__":

    answer = ask_ai(
        "Explain what an IT Program Manager does in one sentence."
    )

    print(answer)