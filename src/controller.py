##This file contains the Controller function.
##It binds the LLM and Validator.

import llm
import validator
import prompts as prp

def asses_llm():
  numtasks = len(prp.questions)
  i = 0
  performance = list()
  while i < numtasks:
    #tasks are hard coded in prompts.py
    #this can be changed such that task is entered by user.
    #in that case fill in the expected_result list in validator.py appropriately.
    #and aslo the condition  of this while loop appropriately.
    task = prp.get_task(i) 
    print(f"TASK: {task}")
    print("====Passing task to LLM=====")
    script = llm.llm_generate_script(task)
    print("====Passing generated script to Validator====")
    performance.append(validator.validate_llm(script))
    i += 1
  return performance

def main():
  assessment = asses_llm()
  print(assessment)

main()

