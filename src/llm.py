
import prompts as prp
import openai
import re

openai.api_key = "PLACE YOUR API KEY HERE"
ai_model = "PLACE MODDEL VERSION HERE"
llm_messages = [ {"role": "system", "content": prp.api_doc()} ]

def llm_generate_script(task):
  llm_messages.append(
          {"role": "user", "content": task},
      )
  print("====Generating script=====")
  # TODO add appropriate error handling.
  chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=llm_messages)
  reply = chat.choices[0].message.content
  llm_messages.append({"role": "assistant", "content": reply})
  return llm_extract_script(reply)

def llm_extract_script(reply):
  match = re.search(r"```(\w+)?(.+?)```", reply, re.DOTALL)
  if match:
    script = match.group(2)
    print("====Script generated====")
    return script.strip()
  else:
    return None
