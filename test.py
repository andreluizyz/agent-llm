import requests

print("Alffex\n")

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
            "prompt": historico
        }
    )

    data = response.json()

    resposta = data["response"]

    historico += f"Alffex: {resposta}\n"

    print("Alffex:", resposta, "\n")