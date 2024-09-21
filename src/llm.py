
import prompts as prp
import openai
llm_messages = [ {"role": "system", "content": prp.api_doc()} ]
def llm_generate_script(task):
  llm_messages.append(
          {"role": "user", "content": task},
      )
  chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=llm_messages)
  reply = chat.choices[0].message.content
  llm_messages.append({"role": "assistant", "content": reply})
  return llm_processes_reply(reply)

def llm_processes_reply(reply):
  script = ""
  return script