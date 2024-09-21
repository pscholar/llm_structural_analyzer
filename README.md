# **Assessing LLM for Structural Analysis of a Simply Supported Beam**

This is a minimalistic project, for which we assess the potential of a LLM for structural analysis of a simply supported beam.  
That is: determination of support reactions, maximum shear, maximum bending moment and visualizing shear and bending moment along the length of the beam.  
The loadings on the beam can be a series uniformly distributed loads and point loads.  
The architecture below was used for the project. The source files  can be found in the **src** folder of this project.

## **Architecture Used**

![Archictecture](llm_architecture.png)

The **LLM** is provided with API documentation of functions and data structures in the **str_analysis** module.  
This module contains functions that know how to perform structural analysis, of a simply supported beam.  
Given a analysis task, the **LLM** is required to generate a script file that contains data structure configuration and api function calls from the **str_analysis** module.  
The generated script is then run by the **Validator**, that then checks the results against expected values.  
The **Validator** assigns a performance level to the **LLM** , and reports result to the **Controller**.

## **Results**

Using the above architecture with ChatGPT 3.5 as the LLM produced 100% rate for the 5 analysis tasks.

## **Discussion**

- The tasks given here were relatively simple.
- However, it demonstrated that with an appropriate architecture,
- These GPTs have the ability to write input data configuration files and scripts,
- calling API of existing structural analysis software to perform structural analysis.
- The ability of these GPTs should be tested more on complex tasks
- in the building construction industry.
- more research is needed to see how these GPTs can be used to
- automate process in the building construction industry
- for more complex tasks a more robust architecture would be required.

## Proposed Robust Architecture

