import os
import sys
import openai


def main():
    if len(sys.argv) < 2:
        print("Uso: python agent_example.py \"mensaje\"")
        sys.exit(1)

    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise SystemExit("Falta la variable OPENAI_API_KEY")

    message = sys.argv[1]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}],
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
