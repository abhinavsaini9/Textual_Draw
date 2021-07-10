# Textual_Draw
Semester Project CSN 252

Problem Statement
-----------------
Draw on textual screen by reading the commands fromstandard input. Type a command (ormore commands) to standard input and press enter toexecute them. Implement the followingcommands.
  *  h : displays help on stdout
  *  w, a, s, d : up, left, down, right 
  *  f : changes drawing symbol to next typed character 
  *  c : clears the screen and returns to center 
  *  p : fills the screen with drawing symbol
  *  q : halt 

<br/>

[SicTools](https://github.com/jurem/SicTools)
---------
Install SicTools to run and simulate the assembly code. Clone source code from the linked git and make the jar using. 

    git clone https://github.com/jurem/SicTools.git
    cd SicTools
    make jar

<br/>

Usage
-----

To run simulator

    java -jar out/make/sictools.jar


Then import the assembly code in the simulator and `Start`.   Follow the help commands to draw which can be seen on the textual screen.

<br/>

Examples
--------

* 'aaaa wwww dddd ssss' -> draws a 4x4 square
* 'f.' -> changes drawing symbol to '.'
* 'f-dddf df-dddf df-ddd' -> draws a dashed line '--- --- ---'

<br/>

Automating 
----------

To input long texts like this, which can be made using [ASCII ART Generator](https://patorjk.com/software/taag)

```
  _______        _              _   _____                     
 |__   __|      | |            | | |  __ \                    
    | | _____  _| |_ __ _ _   _| | | |  | |_ __ __ ___      __
    | |/ _ \ \/ / __/ _` | | | | | | |  | | '__/ _` \ \ /\ / /
    | |  __/>  <| || (_| | |_| | | | |__| | | | (_| |\ V  V / 
    |_|\___/_/\_\\__\__,_|\__,_|_| |_____/|_|  \__,_| \_/\_/  
    
```
<br/>

Use [Script](./Convert.py) and input the text using an [input file](./input.txt) and get the corresponding [output](./output.txt) in form of the commands. Which can be directly pasted on the command line to be run.

<br/>

Other Group Members
-------------------

* [Rahul](https://github.com/rahulag2411)
* [Harsh](https://github.com/harsh1454)
* [Jinendra](https://github.com/Jinendra-verma)
* [Ritikesh]
* [Jatin]
