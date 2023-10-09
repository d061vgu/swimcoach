import os
import t
import openai

# OpenAI API
openai.api_key = os.getenv("")




# 生徒検索
# 練習メニュー提案
def ChatGPT():
    with open('./txt/prompt.txt', 'r', encoding="utf-8") as f:
        prmpt = f.read()

    print(prmpt)

def main():
    print("a")

if __name__ == "__main__":
    main()
