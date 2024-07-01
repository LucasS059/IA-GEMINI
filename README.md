# IA - GEMINI

## Sobre o Projeto

Este projeto demonstra a integração de um chatbot baseado na API Google Generative AI (Gemini). Existem duas formas de usar o chatbot: através do Google Colab e com uma interface web usando Flask. Abaixo você encontrará instruções detalhadas para ambas as abordagens, além de como obter a chave da API necessária.

## Usando o Google Colab
Para testar o chatbot sem usar a interface web, siga os passos abaixo:

1. Baixe o arquivo `IA-GEMINI.ipynb` localizado na pasta `ChatbotColab`.
2. Abra o arquivo no [Google Colab](https://colab.research.google.com/).
3. Insira a chave da API conforme necessário.

### Obtendo a Chave da API

Para obter a chave da API, siga as instruções na seção "Acessar chave da API do Gemini" abaixo.

---

## Usando com a Interface Web

Para usar o chatbot com a interface web, siga estes passos:

1. Baixe o arquivo `chat_gemini.py` e a pasta `templates` que contém o arquivo `index.html`.
2. No terminal, instale as dependências necessárias:
   ```sh
   pip install google-generativeai Flask
   ```
3. Abra o arquivo `chat_gemini.py` e insira sua chave da API.
4. No terminal, execute o seguinte comando:
   ```sh
   python chat_gemini.py
   ```
   Isso iniciará o servidor local e fornecerá um endereço localhost e porta. Copie e cole esse endereço no seu navegador.

---

## Acessar a Chave da API do Gemini

Para acessar a chave da API do Gemini, siga os passos abaixo:

1. Acesse o [link](https://aistudio.google.com/app/prompts/new_chat?utm_source=ai.google.dev&utm_medium=referral&utm_campaign=log_in&pli=1).
2. Na tela principal do site, clique em "Get API Key".
   ![image](https://github.com/LucasS059/IA-GEMINI/assets/133230032/54df79e0-a948-4f97-a7b9-6b3d2709563f)
3. Clique em "Criar chave de API".
   ![image](https://github.com/LucasS059/IA-GEMINI/assets/133230032/262159e7-06e3-4326-a955-d57d464ea19e)
4. Clique na opção azul para confirmar.
   ![image](https://github.com/LucasS059/IA-GEMINI/assets/133230032/bb6d152b-a2a8-4a04-b26b-a4e41e404cd8)
5. Copie a chave gerada e substitua no código conforme necessário.
   ![image](https://github.com/LucasS059/IA-GEMINI/assets/133230032/53e05edd-cebe-48c9-b48a-85fbc45dc8a6)

---

Com essas instruções, você poderá usar o IA-GEMINI tanto no Google Colab quanto na interface web de forma fácil e rápida.

---
