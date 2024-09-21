import json
import os

expected_results = {
  {25,25,10,10},
  {25,25,10,10},
  {25,25,10,10},
  {25,25,10,10},
  {25,25,10,10},
  {25,25,10,10},
  {25,25,10,10},
  {25,25,10,10},
  {25,25,10,10},
  {25,25,10,10},
  {25,25,10,10},
  {25,25,10,10}
}
cur_task = 0
max_error = 0.01

def validate_llm(script):
  script_file = open("llm_generated.py","w")
  script_file.write(script)
  script_file.close()
  os.system("py llm_generated.py")
  results_file = open("results.json","r")
  computed_results = json.load(results_file)
  results_file.close(results_file)
  perfomance = measure_performance(computed_results)
  cur_task += 1
  return perfomance

def measure_performance(computed_results):
  performance = 100.0
  i = 0
  for value in computed_results.values():
    error = abs(value- expected_results[cur_task][i])
    if error > max_error:
      performance -= 25.0
    i += 1
  return performance
