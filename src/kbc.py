questions = [
    ["Q1: What is the capital of France?", 
     "1. Berlin", "2. Madrid", "3. Paris", "4. Rome", 3],

    ["Q2: Which planet is known as the Red Planet?",  
     "1. Earth", "2. Mars", "3. Jupiter", "4. Saturn", 2],

    ["Q3: Who wrote 'To Kill a Mockingbird'?", 
     "1. Harper Lee", "2. J.K. Rowling", "3. Ernest Hemingway", "4. Mark Twain", 1],

    ["Q4: What is the largest ocean on Earth?", 
     "1. Atlantic Ocean", "2. Indian Ocean", "3. Arctic Ocean", "4. Pacific Ocean", 4],

    ["Q5: Who painted the Mona Lisa?", 
     "1. Vincent van Gogh", "2. Pablo Picasso", "3. Leonardo da Vinci", "4. Claude Monet", 3],

    ["Q6: What is the smallest prime number?", 
     "1. 0", "2. 1", "3. 2", "4. 3", 3],

    ["Q7: Which element has the chemical symbol 'O'?", 
     "1. Gold", "2. Oxygen", "3. Silver", "4. Iron", 2],

    ["Q8: Who is known as the Father of Computers?", 
     "1. Charles Babbage", "2. Alan Turing", "3. Bill Gates", "4. Steve Jobs", 1],

    ["Q9: What is the hardest natural substance on Earth?", 
     "1. Gold", "2. Iron", "3. Diamond", "4. Platinum", 3],

    ["Q10: Which country is known as the Land of the Rising Sun?", 
     "1. China", "2. Japan", "3. South Korea", "4. Thailand", 2],

    ["Q11: What is the speed of light?", 
     "1. 300,000 km/s", "2. 150,000 km/s", "3. 450,000 km/s", "4. 600,000 km/s", 1],

    ["Q12: Who developed the theory of relativity?", 
     "1. Isaac Newton", "2. Albert Einstein", "3. Galileo Galilei", "4. Nikola Tesla", 2],

    ["Q13: What is the chemical symbol for gold?", 
     "1. Au", "2. Ag", "3. Pb", "4. Fe", 1],

    ["Q14: Which planet is known as the Earth's twin?", 
     "1. Mars", "2. Venus", "3. Jupiter", "4. Saturn", 2],

    ["Q15: Who is the author of '1984'?", 
     "1. George Orwell", "2. Aldous Huxley", "3. F. Scott Fitzgerald", "4. J.D. Salinger", 1],

    ["Q16: What is the largest mammal?", 
     "1. Elephant", "2. Blue Whale", "3. Giraffe", "4. Hippopotamus", 2],

    ["Q17: What is the main ingredient in guacamole?", 
     "1. Tomato", "2. Avocado", "3. Onion", "4. Pepper", 2],

    ["Q18: Who was the first person to walk on the moon?", 
     "1. Yuri Gagarin", "2. Buzz Aldrin", "3. Neil Armstrong", "4. Michael Collins", 3],
]

prize_levels = [
    1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 
    160000, 320000, 640000, 1250000, 2500000, 5000000, 7500000, 
    10000000, 50000000, 70000000
]
level_milestones = [8, 12, 15]  # Indices where levels change
milestone_prizes = [160000, 2500000, 10000000]  # Prizes for each milestone

total_won = 0
current_level = 0

def play_game():
    global total_won, current_level
    for index, question in enumerate(questions):
        print(question[0])
        for i in range(1, 5):
            print(question[i])
        
        if index == 0:
            answer = input("Please enter your option: ")
        else:
            answer = input("Please enter your option number or type 'quit' to exit: ")
        
        if answer.lower() == 'quit':
            print(f"Congratulations, you have won Rs. {total_won}")
            break
        
        answer = int(answer)
        
        if answer != question[5]:
            print("Wrong answer! Game over.")
            if index > level_milestones[current_level]:
                total_won = milestone_prizes[current_level]
            print(f"You have won Rs. {total_won}")
            break
        else:
            total_won = prize_levels[index]
            print("Correct answer!")
            if index < len(questions) - 1:
                print("Moving to the next question.")
            print(f"You have won Rs. {total_won}")
            
            if index in level_milestones:
                current_level += 1

if __name__ == "__main__":
    play_game()