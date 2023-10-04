from simpleai.search import CspProblem, backtrack
import streamlit as st

def constraint_unique(variables, values):
    return len(values) == len(set(values))

def constraint_add(variables, values):
    factor1 = int("".join(str(values[variables.index(letter)]) for letter in word1))
    factor2 = int("".join(str(values[variables.index(letter)]) for letter in word2))
    result = int("".join(str(values[variables.index(letter)]) for letter in answer))
    return (factor1 + factor2) == result

def format_solution(solution):
    word1_numbers = "".join(str(solution[letter]) for letter in word1)
    word2_numbers = "".join(str(solution[letter]) for letter in word2)
    answer_numbers = "".join(str(solution[letter]) for letter in answer)
    return f"{word1} {word1_numbers}\n + \n{word2} {word2_numbers}\n = \n {answer} {answer_numbers}"

def solve(word1, word2, answer):
    if len(word1) < 9 and len(word2) < 9 and len(answer) < 9:
        letters = tuple(list(set(word1 + word2 + answer)))
        if len(letters) <= 9:
            first_letter_set = set([word1[0], word2[0], answer[0]])
            domains = {letter: (range(1, 10) if letter in first_letter_set else range(10)) for letter in letters}
            constraints = [(letters, constraint_unique), (letters, constraint_add)]
            problem = CspProblem(tuple(letters), domains, constraints)
            solutions = backtrack(problem)
            if solutions:
                return format_solution(solutions)
            else:
                return "No solution found."
        else:
            return "No solution found because there are more than 9 different letters."
    else:
        return "No solution found because the words are too long or too short."

st.title("Solve Cryptoarithmetic Puzzles!")
st.subheader("By Maarten Hens")

word1 = st.text_input('Enter your first word')
word2 = st.text_input('Enter your second word')
answer = st.text_input('Enter your answer')

if st.button('Solve'):
    solutions = solve(word1, word2, answer)
    st.text(solutions)

