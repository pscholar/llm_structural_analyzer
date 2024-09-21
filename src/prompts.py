def api_doc():
  instruction = """
  For the questions to follow, respond only with code.
  Your an intelligent structural analysis assistant. Your duty is to write a python script,
  that calls appropriate functions form the str_analysis module to accomplish the task of calculating 
  support reactions, max bending moment and max shear force, 
  and also draw the shear force and bending moment diagram, for a simply supported beam.
  The script should contain only variable definitions and function calls.
  The documentation of the functions in in the str_analysis is as below:
  """
  doc = """
  calc_support_reactions(beam_length,config):
    - calculates reactions at supports
    - returns a list containing the left and right support reactions
  calc_shear(beam_length,config):
    - calculates shear along the length of the beam.
    - returns a list containing values shear at different lengths along the beam
  calc_bmoment(beam_length,config):
    -calculates bending moment along the lenght of the beam.
    -returns a list containig bending values of shear at different lengths of the beam
  All the above functions take in the arguments described below:
        -beam_length (float): Length of the beam.
        -config (list of dict): List of load configurations, where each load is defined
                              by a dictionary with keys 'lvalue', 'ltype', and 'ldist'.
                              lvalue specifies the value of the load
                              ltype specifies the type of the load that is; U for a uniformly distributed laod
                              and P for a point load
                              ldist specifies the distance of the load from the left support. This value
                              should equal to the length of the beam for a uniformly distributed load.
  calc_max_bmoment(moments):
    -computes the maximum bending moment.
    -Arg: moments- a list of bending moments along the length of the beam.
    -Returns: the maximum bending moment.
  calc_max_shear(shears):
    -computes the maximum shear.
    -Arg: shears- a list of shears along the length of the beam.
    -Returns: the maximum shear.
  draw_shear_diagram(beam_length, shear_values):
    -draws the shear force diagram.
    -Args:
      beam_length: length of the beam
      shear_values: a list of shear values along the length ot the beam.
  draw_moment_diagram(beam_length, moment_values):
    -draws the bending moment diagram.
    -Args:
      beam_length: length of the beam
      shear_values: a list of bending moment values along the length ot the beam.
"""
  return instruction + doc
questions = [
    "A 5m long simply beam carries a uniformly distributed load of 10kN/m \
        and a point load of 5kN at a distance of 3m from the left support. Compute the reactions at supports and maximum bending moment and shear",
    "A beam, 10m long is simply supported and loaded with 10kN/m \
      uniformly distributed load and a point load of 5kN at midspan"
             ]

def load_task(index):
  if(index > len(questions) - 1):
    index = len(questions) - 1
  return[questions[index]]
print(api_doc())