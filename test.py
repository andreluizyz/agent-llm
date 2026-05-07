import requests

print("Alffex iniciado\n")

historico = ""

while True:

    user_input = input("Você: ")

    if user_input.lower() == "sair":
        break

    historico += f"Usuário: {user_input}\n"

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": historico,
            "stream": False
        }
    )

    data = response.json()

    resposta = data["response"]

    historico += f"Alffex: {resposta}\n"

    print(f"\nAlffex: {resposta}\n")