
import prompts as prp
import openai
openai.api_key = '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'
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