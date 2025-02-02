'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
import time

letterGrades = \
    {"A": 93, "A-": 90, "B+": 87, "B": 83, "B-": 80, "C+": 77, "C": 73, "C-": 70, "D+": 67, "D": 63, "D-": 60, "F": 0}

def overallGrade(sem,final,worth) :
    return sem*(1-worth/100) + final*(worth/100)

def toLetterGrade(percent) :
    for i in letterGrades :
        if percent >= letterGrades.get(i) :
            return i

class question():
    def __init__(self, prompt, answers, correctAnswer):
        # correctAnswer is an index of the answers list, not a number
        # if correctAnswer is -1, then ask for an int
        self.prompt = prompt,
        self.answers = answers
        self.correctAnswer = correctAnswer

    def checkAnswer(self):
        answerString = self.answers[self.correctAnswer]
        self.isCorrect = (self.userInput.lower().strip() == answerString.lower()) or (self.userInput == str(self.correctAnswer+1))

        if self.isCorrect:
            print(('\033[92m' + "\nYou are correct! {} is the answer!" + '\033[0m').format(answerString))
        else:
            print("\nThat is incorrect! The correct answer was {}!".format(answerString))
        return self.isCorrect

    def ask(self):
        print("---------------")
        print(('\033[95m' + "{}\n" + '\033[0m').format(self.prompt[0]))

        if self.correctAnswer != -1:
            answerNum = 0
            for a in self.answers:
                answerNum += 1
                print("{}) {}".format(answerNum, self.answers[answerNum-1]))
        else :
            print("Enter your answer:")

        self.userInput = input("\nA: ")
        self.checkAnswer()

        print("---------------\n")
        return self.isCorrect


def main():
    userReady = input("Are you ready? ")

    yesAnswers = ["y","yes","mhm","sure","absolutely","yeah","yea","yup"]

    for i in yesAnswers :
        if userReady.lower() == i:
            print("Ok, let's start!\n")
            break
        elif yesAnswers.index(i) == len(yesAnswers)-1:
            print("Ok goodbye")
            exit()

    allQuestions = [
        question("Q1: Which president came after Abraham Lincoln?", ["Millard Filmore","Andrew Johnson","James Buchanan","Ulysses S. Grant"], 1),
        question("Q2: How do you say hello in Italian?", ["Bonjour", "Hola", "Ciao", "Olá"], 2),
        question("Q3: What is the name of Spongebob's snail?", ["Gibby", "Garret", "Gerald", "Gary"], 3),
        question("Q4: What is the capital of Canada?", ["Ottawa", "Toronto", "Montreal", "Vancouver"], 0),
        question("Q5: 89 - 27 + 5", ["67"], -1),
        question("Q6: 2x + 62 = 74\nSolve for x", ["6"], -1),
        question("Q7: Who is the principal of UHS?", ["Mr. Carver"], -1)
    ]

    correctCount = 0
    wrongCount = 0

    for q in allQuestions:

        askedQuestion = q.ask()
        if askedQuestion:
            correctCount += 1
        else :
            wrongCount += 1

        time.sleep(1)

    percentage = (correctCount/(correctCount + wrongCount)) * 100
    print("Thank you for taking the quiz!\nYou scored a {}% ({})".format(str(percentage)[0:5], toLetterGrade(percentage)))

main()
