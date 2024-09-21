import numpy as np
import matplotlib.pyplot as plt
import prompts as prp
import llm
import validator

numtasks = len(prp.questions)
i = 0
performance = list()
while i < numtasks:
  task = prp.load_task(i)
  print(f"TASK {i}: {task}\n")
  script = llm.llm_generate_script(task)
  performance.append(validator.validate_llm(script))
  i += 1
#plot the performance curve
plt.plot(np.array(performance))
plt.xlabel("Task Label")
plt.ylabel("Performance(%)")
plt.title("Performance Level for Each Task")
plt.show()


