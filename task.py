
from simpleai.search import CspProblem, backtrack
import streamlit as st

word1 = ""
word2 = ""
answer = ""
output = ""

# each number has to be unique
def constraint_unique(variables, values):
    return len(values) == len(set(values))  # remove repeated values and count

# constraint to check if word1 + word 2 = answer
def constraint_add(variables, values):
    factor1 = "";
    #for each letter of the word search the value in the values array
    for letter in word1:
        factor1 += str(values[variables.index(letter)])
    factor1 = int(factor1)
    factor2 = "";
    #for each letter of the word search the value in the values array
    for letter in word2:
        factor2 += str(values[variables.index(letter)])
    factor2 = int(factor2)
    result = "";
    #for each letter of the word search the value in the values array
    for letter in answer:
        result += str(values[variables.index(letter)])   
    result = int(result)

    return (factor1 + factor2) == result

def solve():

    # check if any of the words are longer than 9 letters or if they are empty, if that's the case there is no valid solution
    if( len(word1) < 9 and len(word1) > 0 and len(word2) < 9 and len(word2) > 0 and len(answer) < 9 and len(answer) > 0) :
        firstLetterArray = []
        firstLetterArray += word1[0]
        firstLetterArray += word2[0]
        firstLetterArray += answer[0]
        lst = list((set(word1 + word2 + answer)))
        variables = tuple(lst)
            # check if there are more then 9 different letters, in that case there is no valid solution
        if(len(variables) < 9):
            domains = {}
            for element in lst:
                if element in firstLetterArray:
                    domains[element] = range(1, 10)
                else: 
                    domains[element] = range(0, 10)

            constraints = [
            (variables, constraint_unique),
            (variables, constraint_add),
            ]
            problem = CspProblem(variables, domains, constraints)
            output = backtrack(problem)
            print('\nSolutions:', output)
        else:
            output = "No solution was found because there are more than 9 different letters!"
    else:
        output = "No solution found because the words are too long or too short!"
    #show the output in a textfield
    st.text(output)

#streamlit app design
st.title("Solve Cryptoarithmetic Puzzles!")
st.subheader("By Maarten Hens")
word1 = st.text_input('Enter your first word')
word2 = st.text_input('Enter your second word')
answer = st.text_input('Enter your answer')

#once the button is pressed run the function
if st.button('Solve'):
    solve()

