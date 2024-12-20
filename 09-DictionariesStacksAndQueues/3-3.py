import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
   correctness_check = queue.LifoQueue()
   for character in expression:
      if is_open_bracket(character):
         correctness_check.put(character)
      elif is_closed_bracket(character):
         char_from_stack = correctness_check.get()
         if is_matching_bracket(char_from_stack, character) == False:       
            return False
   return correctness_check.empty() #True if brackets in expression are ok of False otherwise

def is_open_bracket(symbol):
   result = symbol == "[" or symbol == "{" or symbol == "("
   return result

def is_closed_bracket(symbol):
   result = symbol == "]" or symbol == "}" or symbol == ")"
   return result

def is_matching_bracket(open_bracket, closed_bracket):
   if open_bracket == "[":
      return closed_bracket == "]"
   elif open_bracket == "{":
      return closed_bracket == "}"
   elif open_bracket == "(":
      return closed_bracket == ")"
   else:
      return False
   



if brackets_ok(expression1):
   print(f"The brackets in expression 1 ({expression1}) are correct.")
else:
   print(f"The brackets in expression 1 ({expression1}) are NOT correct.")

if brackets_ok(expression2):
   print(f"The brackets in expression 2 ({expression2}) are correct.")
else:
   print(f"The brackets in expression 2 ({expression2}) are NOT correct.")

if brackets_ok(expression3):
   print(f"The brackets in expression 3 ({expression3}) are correct.")
else:
   print(f"The brackets in expression 3 ({expression3}) are NOT correct.")