#This file contains functions that interface with openai API

import prompts as prp
import openai
import re
import os

#assume the key and model  to use are stored in environment variables.
# TODO add error handling when None is returned
openai.api_key = os.environ.get('OPENAI_API_KEY')
ai_model = os.environ.get('OPENAI_GPT_MODEL')
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
