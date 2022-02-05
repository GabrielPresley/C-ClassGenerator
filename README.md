# C-ClassGenerator
## How it works
After running the python file a number of questions are asked,      
these questions are used to automatically generate a class file       
with minimum user input required      

## Basic Inputs
```
CLASS NAME: 
DEFAULT LIBS? (bool): 
GETS FOR ALL VARS? (bool): 
SETS FOR ALL VARS? (bool): 
NUMBER OF VARS: 
VARIABLE NAME: 
VARIABLE NAME: 
NUMBER OF FUNCTIONS: 
FUNCTION NAME: 
FUNCTION NAME: 
TEST (bool): 
NUMBER OF TESTS: 
```


example input:
```
ClassName
1
1
1
2
variableNumberOne
VariableNumberTwo
2
FunctionNumberOne
FunctionNumberTwo
1
2

```
## Generated Code:

```CPP
#include <iostream>
#include <string>
using namespace std;


class  ClassName {
	public:
		 (//TODO TYPE) variableNumberOne
		 (//TODO TYPE) VariableNumberTwo



	void getVariablenumberone(){
		return  variableNumberOne
	}
	void getVariablenumbertwo(){
		return  VariableNumberTwo
	}
	//TODO TYPE setVariablenumberone(//TODO TYPE INPUT){
		 variableNumberOne  = INPUT
	}
	//TODO TYPE setVariablenumbertwo(//TODO TYPE INPUT){
		 VariableNumberTwo  = INPUT
	}
	 FunctionNumberOne(){
		//TODO FUNCTION BODY
	}
	 FunctionNumberTwo(){
		//TODO FUNCTION BODY
	}


int main(){
	 ClassName ClassName0
	 ClassName ClassName1



	 ClassName0.setvariableNumberOne();
	 ClassName1.setVariableNumberTwo();



	cout << ClassName0.getvariableNumberOne();
	cout << ClassName1.getVariableNumberTwo();



	FunctionNumberOne();
	FunctionNumberTwo();
}
```
