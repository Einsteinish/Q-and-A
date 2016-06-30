# Q3 

def isBalanced(test):
  st = []
  for b in test:
    if b == '(':
      st.append(b)
    elif b == ')':
      if st[-1] != '(':
        return False
      else:
         st.pop()
    if b == '{':
      st.append(b)
    elif b == '}':
      if st[-1] != '{':
        return False
      else:
         st.pop()
    if b == '[':
      st.append(b)
    elif b == ']':
      if st[-1] != '[':
        return False
      else:
        st.pop()

  # openings popped off yet, return False
  if st: 
    return False

  # passed the check, return True  
  return True


if __name__ == '__main__':
  test = ['[](){}', '([)]' , '({[]})', '[()]{{}}', '[[())]]', '(({})[])', '()(()', '(()(']  
  bal = True
  for t in test:
     bal = isBalanced(t)
     print("%s is balanced? %s" %(t, bal))


'''
OUTPUT

[](){} is balanced? True
([)] is balanced? False
({[]}) is balanced? True
[()]{{}} is balanced? True
[[())]] is balanced? False
(({})[]) is balanced? True
()(() is balanced? False
(()( is balanced? False
'''

