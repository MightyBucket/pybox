
### CREATED BY DARYL CECILE > GITHUB: DARCECTECH
## YOU MAY USE AND AMMEND THE CODE AS LONG AS IT IS MADE EXPLICIT IN NEW ITERATIONS
## IF YOU HAVE ANY SUGGESTIONS, PLEASE LET ME KNOW.
## I AM PLANNING TO CHANGE THE LICENSE TO MIT-LICENSE FOR THIS PROJECT ONCE IT IS COMPLETE
## PLEASE READ THE BITS OF INFORMATION AT THE BOTTOM OF THIS CODE

## THIS FILE IS THE POSTPROCESSOR FOR THE TOKENS THAT ARE CREATED BY THE PLEXER
## IT DETECTS AND SPLITS UP JOINED TOKENS SO THAT THEY CAN BE IDENTIFIED INDIVIDUALLY
## IT ALSO PERFORMS KEYWORD MIS-ALIGNMENT THAT WAS CAUSED BY DELETION OF REPEATED TOKENS

class postProcessor():
	def __init__():
		print("DBUG: PostProcessor Active.")

	def process(tokens):
		print("DBUG: Processing tokens. . .")
		currentIndex = -1
		lastItem = ""
		for toke in tokens[0]:
			currentIndex +=1
			if len(tokens[0])>1 and toke == "__no_token":
				# tokens[0].pop(0)
				# tokens[1].pop(0)
				# tokens[2].pop(0)
				# tokens[3].pop(0)
				# WHETHER THE ABOVE IS REQUIRED IS NOT ENTIRELY CLEAR
				print("",end="")
			if str((toke).encode('utf8'))[2:-1].startswith("\\t") and len(str((toke).encode('utf8'))[2:-1])>3:
				## Had to do this to split tabs from variables and such objects
				tokens[0][currentIndex] = tokens[0][currentIndex][1:]
				tokens[0].insert(currentIndex,"\t")
				tokens[1].insert(currentIndex,tokens[1][currentIndex])
				tokens[2].insert(currentIndex,tokens[1][currentIndex]+1)
				tokens[3].insert(currentIndex,"TAB")
				print("INFO: Token '"+toke+"' was split into '\\t' and '"+tokens[0][currentIndex+1]+"'. ReProcessing. . .")
				return False
				break
			if (toke == lastItem):
				print("INFO: Similar token '"+toke+"' was found and was removed.")
				## Happens too frequently so we have to capture it before it hurts someone
				del tokens[0][int(currentIndex)]
				del tokens[1][int(currentIndex)]
				del tokens[2][int(currentIndex)]
				del tokens[3][int(currentIndex)]
				return False
				break
			if (tokens[3][currentIndex] != "STRING") and (" " in toke):
				## This happens a lot with function definition so we want to catch these out!
				values = []
				values.append(toke.split(" ")[0])
				values.append(toke.split(" ")[1])
				if values[0] == lastItem:
					tokens[0][currentIndex] = values[1]
				print("INFO: Similar content in '"+toke+"' was found. Corrections were made.")
			if (tokens[3][currentIndex] == "VARIABLE") and (toke.startswith("'") or toke.startswith('"')):
				## This happens with strings that start straight after a tab
				del tokens[0][int(currentIndex)]
				del tokens[1][int(currentIndex)]
				del tokens[2][int(currentIndex)]
				del tokens[3][int(currentIndex)]
				print("INFO: Accidental conversion of start of string to variable detected with '"+toke+"'. Corrections were made.")
				return False
			if (tokens[3][currentIndex]=="VARIABLE" and toke == "def"):
				tokens[3][currentIndex] = "FUNCTION_DECLARATION"
				print("INFO: Mis-alignment of keywords in token. '"+toke+"' was recognised as a VARIABLE instead of a FUNCTION_DECLARATION. Corrections were made.")
			if (tokens[3][currentIndex]=="VARIABLE" and toke == "print"):
				tokens[3][currentIndex] = "KEYWORD"
				print("INFO: Mis-alignment of keywords in token. '"+toke+"' was recognised as a VARIABLE instead of a KEYWORD. Corrections were made.")
			lastItem = str(toke)