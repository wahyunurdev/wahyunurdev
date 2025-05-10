import openai
import time

def read_questions(file_path):
    """從指定路徑讀取問題，每行一個問題"""
    with open(file_path, 'r', encoding='utf-8') as file:
        questions = file.readlines()
    questions = [q.strip() for q in questions]
    return questions

def append_answer(file_path, answer):
    """将单个答案追加到指定的文件"""
    with open(file_path, 'a', encoding='utf-8') as file:  # 使用追加模式 'a'
        file.write(answer + '\n')

def truncate_question(question, max_length=5400):
    """根据最大 token 数预处理并截断问题"""
    # 估算每个 token 大约代表的字符数，这里假设为 4
    estimated_chars_per_token = 4
    max_chars = max_length * estimated_chars_per_token
    if len(question) > max_chars:
        print("Question length exceeds limit, truncating...")
        return question[:max_chars]
    return question

def ask_chatgpt(question, api_key):
    """使用 ChatGPT API 提問並獲得答案"""
    openai.api_key = api_key
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            #max_tokens=8192,
            temperature=0.2,
            messages=[
                {"role": "user", "content": question},
            ]
        )
        answer = response.choices[0].message.content
        return answer
    except openai.error.RateLimitError:
        print("Rate limit exceeded, waiting...")
        time.sleep(60)  # 等待 60 秒
        return ask_chatgpt(question, api_key)  # 重新尝试
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "Error: Unable to process the question."

def main():
    api_key = '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' # 替換成你的 API key
    prompt_prefix = '你是一位老師，請你跟我說，下面的文章是1到12年級，哪一個年級的學生適合閱讀，你只要回應我特定的年級值即可，不需要說明原因：'  # 特定提示词
    questions_file_path = 'questions.txt' # 問題檔案路徑
    answers_file_path = 'answers.txt' # 答案檔案路徑

    questions = read_questions(questions_file_path)
    answers = []

    for question in questions:
        full_question = prompt_prefix + truncate_question(question)  # 将提示词和问题合并
        answer = ask_chatgpt(full_question, api_key)
        time.sleep(10)
        append_answer(answers_file_path, answer)

if __name__ == '__main__':
    main()
