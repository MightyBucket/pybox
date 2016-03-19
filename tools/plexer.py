
### CREATED BY DARYL CECILE > GITHUB: DARCECTECH
## YOU MAY USE AND AMMEND THE CODE AS LONG AS IT IS MADE EXPLICIT IN NEW ITERATIONS
## IF YOU HAVE ANY SUGGESTIONS, PLEASE LET ME KNOW.
## I AM PLANNING TO CHANGE THE LICENSE TO MIT-LICENSE FOR THIS PROJECT ONCE IT IS COMPLETE
## PLEASE READ THE BITS OF INFORMATION AT THE BOTTOM OF THIS CODE

tokens = [["content"],[0],[0],["type"]]
errors = [["message"],["type"],[0]]

def parseIntoTokens(theString):
	clearReg()
	print("Starting parser. . . ")
	lastContent = ""
	currentLetter = ""
	previousLetter = ""
	isStringOpen = False
	stringOpenAt = 0
	stringOpenWith = ""
	for i in range(0,len(theString)):
		# For each index of every letter
		currentLetter = theString[i]
		previousLetter = theString[i] if i == 0 else theString[i-1]
		if isStringOpen == False and currentLetter == " ":
			print("space out of place")
		elif isStringOpen == False and currentLetter.isdigit() and theString[i-1].isdigit() == False:
			print("found digit")
			value = str(currentLetter)
			end = False
			ic = i
			while end == False:
				if len(theString)> (ic+1):
					ic+=1
				else:
					end = True

				if end == False and theString[ic].isdigit():
					value += str(theString[ic])
				else:
					end = True
			tokens[0].append(value)
			tokens[1].append(i)
			tokens[2].append(ic)
			tokens[3].append("INTEGER")
		elif isStringOpen == False and currentLetter == "\"":
			isStringOpen = True
			stringOpenWith = "\""
			addToken("\"",i,i+1,"DOUBLEQUOTE")
			stringOpenAt = i
		elif isStringOpen == True and stringOpenWith == "\"" and currentLetter == "\"":			
			stringLength = i - stringOpenAt
			value = theString[stringOpenAt+1:stringOpenAt + stringLength]
			addToken(value,stringOpenAt,i,"STRING")
			isStringOpen = False
			addToken("\"",i,i+1,"DOUBLEQUOTE")
		elif isStringOpen == False and currentLetter == "\'":
			isStringOpen = True
			stringOpenWith = "\'"
			addToken("\'",i,i+1,"SINGLEQUOTE")
			stringOpenAt = i
		elif isStringOpen == True and stringOpenWith == "\'" and currentLetter == "\'":			
			stringLength = i - stringOpenAt
			value = theString[stringOpenAt+1:stringOpenAt + stringLength]
			addToken(value,stringOpenAt,i,"STRING")
			isStringOpen = False
			addToken("\'",i,i+1,"SINGLEQUOTE")
		elif isStringOpen == False and currentLetter == "=" and theString[i-1] != "=":
			if theString[i+1] == "=" and theString[i+2] != "=":
				addToken("==",i,i+2,"IF_EQUALS")
			elif theString[i+1] == "=" and theString[i+2] == "=":
				addToken("===",i,i+3,"IS_EQUIVALENT")
			else:
				addToken("=",i,i+1,"EQUALS")
		elif isStringOpen == False and currentLetter == "T" and theString[i-1] == " ":
			if theString[i:i + 4] == "True":
				addToken("TRUE",i,i+4,"BOOLEAN")
			else:
				end = False
				value = ""
				ic = i
				while end == False:
					if len(theString)> (ic+1):
						ic+=1
					else:
						end = True
	
					if end == False and theString[ic] != " ":
						value += theString[ic]
					else:
						end = True
				addToken(value,i,ic,"VARIABLE")
		elif isStringOpen == False and currentLetter == "F" and theString[i-1] == " ":
			if theString[i:i + 5] == "False":
				addToken("FALSE",i,i+5,"BOOLEAN")
			else:
				end = False
				value = ""
				ic = i
				while end == False:
					if len(theString)> (ic+1):
						ic+=1
					else:
						end = True
	
					if end == False and theString[ic] != " ":
						value += theString[ic]
					else:
						end = True
				addToken(value,i,ic,"VARIABLE")
		elif isStringOpen == False and currentLetter == "d" and theString[i:i + 3] == "def":
			addToken("def",i,i+3,"FUNCTION_DECLARATION")
			end = False
			name = ""
			ic = i+3
			while end == False:
				if len(theString)> (ic+1):
					ic+=1
				else:
					end = True

				if end == False and theString[ic] != " " and theString[ic] != "(":
					name += theString[ic]
				else:
					end = True
			if name != "":
				addToken(name,i,ic,"FUNCTION_NAME")
			else:
				logError("Missing function name","NO_DEF_NAME",i)
		elif tokens[3][-1] != "FUNCTION_NAME" and isStringOpen == False and currentLetter != "=" and currentLetter!="(" and currentLetter!=")" and (theString[i-1] == " " or theString[i-1] == "=" or theString[i-1] == "(" or i ==0 ):
			print(currentLetter)
			end = False
			value = theString[i]
			ic = i
			while end == False:
				if len(theString)> (ic+1):
					ic+=1
				else:
					end = True

				if end == False and theString[ic] != " " and theString[ic] != ")":
					value += theString[ic]
				else:
					end = True
			addToken(value,i,ic,"VARIABLE")
		elif isStringOpen == False and currentLetter == "(" and tokens[3][-1] == "FUNCTION_NAME":
			addToken("(",i,i+1,"LEFT_PAREN")
		elif isStringOpen == False and currentLetter == ")" and (tokens[3][-1] == "FUNCTION_PARAMETER" or tokens[3][-1] == "LEFT_PAREN"):
			addToken(")",i,i+1,"RIGHT_PAREN")
		elif isStringOpen == False and len(tokens[3])>3:
			if tokens[3][-3] == "FUNCTION_DECLARATION" and tokens[3][-1] == "LEFT_PAREN":
				end = False
				value = ""
				ic = i
				while end==False:
					if len(theString)> (ic+1):
						ic+=1
					else:
						end = True
	
					if end == False and theString[ic] != ")":
						if theString[ic] == ",":
							addToken(value,i,ic,"FUNCTION_PARAMETER")
							value = ""
						else:
							value += theString[ic]
					else:
						end = True
						addToken(value,i,ic,"FUNCTION_PARAMETER")
	print("Parsing complete!")
	cleanReg()

def cleanReg():
	del tokens[0][0]
	del tokens[1][0]
	del tokens[2][0]
	del tokens[3][0]
	if len(errors[0])>1:
		del errors[0][0]
		del errors[1][0]
		del errors[2][0]

def clearReg():
	tokens = [["content"],[0],[0],["type"]]
	errors = [["message"],["type"],[0]]

def addToken(val,startPos,endPos,typeX):
	tokens[0].append(val)
	tokens[1].append(startPos)
	tokens[2].append(endPos)
	tokens[3].append(typeX)

def logError(message,typeX,loc):
	errors[0].append(message)
	errors[1].append(typeX)
	errors[2].append(loc)
	print("ERR at "+ str(loc) + ": " + typeX + " > " + message)


## NOTES:
## Currently having some difficulties differentiating between variables and function-parameters and parameter values
## To parse statements into tokens, call the parseIntoTokens function, passing the statements as string as parameters
## At current, parsing will have to be done line by line for correct syntax

print(tokens)
print(errors)