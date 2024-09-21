##contains functions that can be called to perform structural analysis
##of a simply supported beam, with uniform loading , point loading 
## or both.

import json
import os
import numpy as np
import matplotlib.pyplot as plt

#number of points along the beam length
str_analysis_resolution = 1000 

#dictionary against which validation is to be made.
results ={
  "l_reaction": 0,
  "r_reaction":0,
  "max_shear": 0,
  "max_moment":0
}

def create_load_config(type,value, distance):
  load_config = {
    "ltype": type,
    "lvalue": value,
    "ldist": distance
  }
  return load_config

def calc_reactions_pld(beam_length,load_config):
  """
  computes ractions at supports due to point load
  """
  reactions = [0.0] * 2
  reactions[0] = load_config["lvalue"] * (beam_length - load_config["ldist"]) / beam_length
  reactions[1] = load_config["lvalue"] - reactions[0]
  return reactions

def calc_reactions_udl(beam_length, udl_load_config):
  """
  computes reactions at supports due to uniformly distributed load
  """
  if  beam_length != udl_load_config["ldist"]:
    ##handle this error, only a full udl is supported
    print("Unsupported UDL configuration\n");
  #compute point load from UDL
  reactions = [0.0] * 2
  reactions[0] = reactions[1] = udl_load_config["lvalue"] * beam_length / 2
  return reactions
  
def superpose_reactions(reactions):
  """
  superposes reaction from different load considerations
  """
  R1 = 0.0
  R2 = 0.0
  for item in reactions:
    R1 += item[0]
    R2 += item[1]
  return [R1,R2]

def calc_support_reactions(beam_length,config):
  """
  computes reactions at supports
  """
  reactions = list()
  for load_config in config:
    if load_config["ltype"] == "P":
      reactions.append (calc_reactions_pld(beam_length,load_config ))
    elif load_config["ltype"] == "U":
      reactions.append (calc_reactions_udl(beam_length,load_config))
    else:
      print("Unknown Load Type") 
  sreactions =  superpose_reactions(reactions) 
  results["l_reaction"] = sreactions[0]
  results["r_reaction"] = sreactions[1]
  return sreactions

def calc_shear_pld(beam_length,pld_load_config):
  shear = list()
  reactions = calc_reactions_pld(beam_length, pld_load_config)
  increment = beam_length / str_analysis_resolution
  i = 0
  while i <= beam_length:
    if i < pld_load_config["ldist"]:
      val = reactions[0]
    else:
      val = reactions[0] - pld_load_config["lvalue"]
    shear.append(val)
    i += increment
  return shear

def calc_shear_udl(beam_length,udl_load_config):
  shear = list()
  indexes = list()
  reactions = calc_reactions_udl(beam_length, udl_load_config)
  increment = beam_length / str_analysis_resolution
  i = 0
  while i <= beam_length:
    val = reactions[0] - udl_load_config["lvalue"] * i
    shear.append(val)
    indexes.append(i)
    i += increment 
  return shear

def superpose_shears(shears):
  sum = [0] * len(shears[0]) 
  for shear in shears:
    i = 0
    for val in shear:
      sum[i] += val
      i += 1
  return sum

def calc_shear(beam_length,config):
  shears = list()
  for load_config in config:
    if load_config["ltype"] == "P":
      shears.append (calc_shear_pld(beam_length,load_config ))
    elif load_config["ltype"] == "U":
      shears.append (calc_shear_udl(beam_length,load_config))
    else:
      print("Unknown Load Type")
  return superpose_shears(shears)

def calc_max_shear(shear):
  ## TODO: change logic to return index of the maximum absoulte value
  ## The maximum shear should be returned without change of sign.
  max_shear = abs(shear[0])
  for val in shear:
    if abs(val) > max_shear:
      max_shear = abs(val)
  results["max_shear"] = max_shear
  return max_shear

def calc_bmoments_pld(beam_length,pld_load_config):
  reactions = calc_reactions_pld(beam_length, pld_load_config)
  moments = list()
  increment = beam_length / str_analysis_resolution
  i = 0
  while i <= beam_length:
    if i < pld_load_config["ldist"]:
      val = reactions[0] * i
    else:
      val = reactions[0] * i - pld_load_config["lvalue"] * ( i - pld_load_config["ldist"])
    moments.append(val)
    i += increment
  return moments

def calc_bmoments_udl(beam_length, udl_load_config):
  moments = list()
  increment = beam_length / str_analysis_resolution
  i = 0
  while i <= beam_length:
    val = 0.5 * udl_load_config["lvalue"] * i * (beam_length - i)
    moments.append(val)
    i += increment
  return moments

def superpose_bmoments(moments):
  sum = [0] * len(moments[0])  
  for moment in moments:
    i = 0
    for val in moment:
      sum[i] += val
      i += 1
  return sum

def calc_bmoment(beam_length,config):
  moments = list()
  for load_config in config:
    if load_config["ltype"] == "P":
      moments.append (calc_bmoments_pld(beam_length,load_config ))
    elif load_config["ltype"] == "U":
      moments.append (calc_bmoments_udl(beam_length,load_config))
    else:
      print("Unknown Load Type")
  return superpose_bmoments(moments)

def calc_max_bmoment(bmoment):
  max_moment = bmoment[0]
  ## TODO: change logic to get index of the maximum absoulte value
  ## The maximum bending moment should be returned without change of sign.
  for val in bmoment:
    if abs(val) > max_moment:
      max_moment = abs(val)
  results["max_moment"] = max_moment
  return max_moment

def plot_graph(xpoints, ypoints, title,xlabel, ylabel):
  plt.plot(xpoints, ypoints)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.title(title)
  plt.show()

def draw_shear_diagram(beam_length, shear_values):
  xpoints = list()
  increment = beam_length / 1000
  i = 0
  while i <= beam_length:
    xpoints.append(i)
    i += increment
  plot_graph(np.array(xpoints), np.array(shear_values),"SFD","x(m)","V(kN)");
  
def draw_moment_diagram(beam_length, moment_values):
  xpoints = list()
  increment = beam_length / 1000
  i = 0
  while i <= beam_length:
    xpoints.append(i)
    i += increment
  plot_graph(np.array(xpoints), np.array(moment_values),"BMD","x(m)","M(kNm)");

#save results json
def save_results():
  with open("results.json","w") as file:
    json.dump(results,file,indent=4)
    file.close()

def main():
  beam_length = 5
  i = 0
  while i < 5:
    config = list()
    #config.append(create_load_config("U",10.0,5))
    config.append(create_load_config("P",10.0,2.5))
    reactions = calc_support_reactions(beam_length,config)
    print(reactions)
    shear = calc_shear(beam_length,config)
    max_shear = calc_max_shear(shear)
    print(max_shear)
    #max_moment = calc_max_bmoment(beam_length,config)
    #print(max_moment)
    os.system("py analyze.py")
    i += 1
main()


  





















  
