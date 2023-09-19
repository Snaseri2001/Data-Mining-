import openai
import pandas as pd


University_data = pd.read_csv(
    "sample.csv")

user_uni = input("Enter The university :")
user_program = input("Enter The program you want :")

filtered_df = University_data[(University_data['university_name'] == user_uni) & (
    University_data['program_name'] == user_program)]

# extract the keys column as a list
keywords = filtered_df['Keys'].tolist()

openai.api_key = "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"


requestt = f"Write Statement of purpose for {user_uni} With This list of keywords {keywords} , this Statement of purpose  more than 200 words please "
print(requestt)
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a chatbot"},
        {"role": "user", "content": requestt},
    ]
)

result = ''
for choice in response.choices:
    result += choice.message.content
result.find("Data Mining")
with open("Sop.txt", "w") as file:
    file.write(result)
    file.close()
