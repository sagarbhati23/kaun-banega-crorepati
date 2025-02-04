import random
# List of questions with options and correct answers
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
    ["Q19: What is the tallest mountain in the world?", 
     "1. K2", "2. Kangchenjunga", "3. Mount Everest", "4. Lhotse", 3],

    ["Q20: Who invented the telephone?", 
     "1. Alexander Graham Bell", "2. Thomas Edison", "3. Nikola Tesla", "4. Guglielmo Marconi", 1],

    ["Q21: What is the smallest country in the world?", 
     "1. Monaco", "2. Vatican City", "3. San Marino", "4. Liechtenstein", 2],

    ["Q22: What is the longest river in the world?", 
     "1. Amazon River", "2. Nile River", "3. Yangtze River", "4. Mississippi River", 2],

    ["Q23: Who discovered penicillin?", 
     "1. Alexander Fleming", "2. Marie Curie", "3. Louis Pasteur", "4. Gregor Mendel", 1],

    ["Q24: What is the capital of Australia?", 
     "1. Sydney", "2. Melbourne", "3. Canberra", "4. Brisbane", 3],

    ["Q25: Who wrote 'Pride and Prejudice'?", 
     "1. Jane Austen", "2. Emily Brontë", "3. Charles Dickens", "4. William Shakespeare", 1],

    ["Q26: What is the largest desert in the world?", 
     "1. Sahara Desert", "2. Arabian Desert", "3. Gobi Desert", "4. Kalahari Desert", 1],

    ["Q27: Who was the first President of the United States?", 
     "1. Thomas Jefferson", "2. Abraham Lincoln", "3. George Washington", "4. John Adams", 3],

    ["Q28: What is the chemical symbol for water?", 
     "1. H2O", "2. CO2", "3. O2", "4. NaCl", 1],

    ["Q29: Who painted the ceiling of the Sistine Chapel?", 
     "1. Michelangelo", "2. Leonardo da Vinci", "3. Raphael", "4. Donatello", 1],

    ["Q30: What is the largest planet in our solar system?", 
     "1. Earth", "2. Mars", "3. Jupiter", "4. Saturn", 3],

    ["Q31: Who wrote 'The Odyssey'?", 
     "1. Homer", "2. Virgil", "3. Sophocles", "4. Euripides", 1],

    ["Q32: What is the capital of Canada?", 
     "1. Toronto", "2. Vancouver", "3. Ottawa", "4. Montreal", 3],

    ["Q33: Who discovered America?", 
     "1. Christopher Columbus", "2. Ferdinand Magellan", "3. Marco Polo", "4. Vasco da Gama", 1],

    ["Q34: What is the largest bone in the human body?", 
     "1. Femur", "2. Tibia", "3. Humerus", "4. Radius", 1],

    ["Q35: Who wrote 'Hamlet'?", 
     "1. William Shakespeare", "2. Charles Dickens", "3. Mark Twain", "4. J.K. Rowling", 1],

    ["Q36: What is the capital of Italy?", 
     "1. Venice", "2. Milan", "3. Rome", "4. Florence", 3],

    ["Q37: Who invented the light bulb?", 
     "1. Thomas Edison", "2. Nikola Tesla", "3. Alexander Graham Bell", "4. George Westinghouse", 1],

    ["Q38: What is the largest continent?", 
     "1. Africa", "2. Asia", "3. Europe", "4. North America", 2],

    ["Q39: Who wrote 'The Great Gatsby'?", 
     "1. F. Scott Fitzgerald", "2. Ernest Hemingway", "3. J.D. Salinger", "4. John Steinbeck", 1],

    ["Q40: What is the capital of Japan?", 
     "1. Beijing", "2. Seoul", "3. Tokyo", "4. Bangkok", 3],

    ["Q41: Who discovered gravity?", 
     "1. Albert Einstein", "2. Isaac Newton", "3. Galileo Galilei", "4. Johannes Kepler", 2],

    ["Q42: What is the largest island in the world?", 
     "1. Greenland", "2. New Guinea", "3. Borneo", "4. Madagascar", 1],

    ["Q43: Who wrote 'Moby-Dick'?", 
     "1. Herman Melville", "2. Nathaniel Hawthorne", "3. Edgar Allan Poe", "4. Mark Twain", 1],

    ["Q44: What is the capital of Russia?", 
     "1. St. Petersburg", "2. Moscow", "3. Novosibirsk", "4. Yekaterinburg", 2],

    ["Q45: Who invented the airplane?", 
     "1. Wright Brothers", "2. Leonardo da Vinci", "3. Samuel Morse", "4. Alexander Graham Bell", 1],

    ["Q46: What is the smallest continent?", 
     "1. Europe", "2. Australia", "3. Antarctica", "4. South America", 2],

    ["Q47: Who wrote 'The Catcher in the Rye'?", 
     "1. J.D. Salinger", "2. F. Scott Fitzgerald", "3. Ernest Hemingway", "4. John Steinbeck", 1],

    ["Q48: What is the capital of Germany?", 
     "1. Munich", "2. Frankfurt", "3. Berlin", "4. Hamburg", 3],

    ["Q49: Who discovered radioactivity?", 
     "1. Marie Curie", "2. Albert Einstein", "3. Niels Bohr", "4. Enrico Fermi", 1],

    ["Q50: What is the largest lake in the world?", 
     "1. Caspian Sea", "2. Lake Superior", "3. Lake Victoria", "4. Lake Huron", 1],

    ["Q51: Who wrote 'War and Peace'?", 
     "1. Leo Tolstoy", "2. Fyodor Dostoevsky", "3. Anton Chekhov", "4. Ivan Turgenev", 1],

    ["Q52: What is the capital of Brazil?", 
     "1. Rio de Janeiro", "2. São Paulo", "3. Brasília", "4. Salvador", 3],

    ["Q53: Who invented the World Wide Web?", 
     "1. Tim Berners-Lee", "2. Bill Gates", "3. Steve Jobs", "4. Mark Zuckerberg", 1],

    ["Q54: What is the smallest planet in our solar system?", 
     "1. Mercury", "2. Venus", "3. Mars", "4. Pluto", 1],

    ["Q55: Who wrote 'The Divine Comedy'?", 
     "1. Dante Alighieri", "2. Geoffrey Chaucer", "3. John Milton", "4. William Blake", 1],

    ["Q56: What is the capital of India?", 
     "1. Mumbai", "2. New Delhi", "3. Kolkata", "4. Chennai", 2],

    ["Q57: Who discovered the structure of DNA?", 
     "1. James Watson and Francis Crick", "2. Rosalind Franklin", "3. Gregor Mendel", "4. Linus Pauling", 1],

    ["Q58: What is the largest animal in the world?", 
     "1. African Elephant", "2. Blue Whale", "3. Great White Shark", "4. Giraffe", 2],

    ["Q59: Who wrote 'The Iliad'?", 
     "1. Homer", "2. Virgil", "3. Sophocles", "4. Euripides", 1],

    ["Q60: What is the capital of Egypt?", 
     "1. Cairo", "2. Alexandria", "3. Giza", "4. Luxor", 1],

    ["Q61: Who invented the printing press?", 
     "1. Johannes Gutenberg", "2. Benjamin Franklin", "3. Thomas Edison", "4. Alexander Graham Bell", 1],

    ["Q62: What is the smallest ocean in the world?", 
     "1. Atlantic Ocean", "2. Indian Ocean", "3. Arctic Ocean", "4. Southern Ocean", 3],

    ["Q63: Who wrote 'The Brothers Karamazov'?", 
     "1. Fyodor Dostoevsky", "2. Leo Tolstoy", "3. Anton Chekhov", "4. Ivan Turgenev", 1],

    ["Q64: What is the capital of South Korea?", 
     "1. Seoul", "2. Busan", "3. Incheon", "4. Daegu", 1],

    ["Q65: Who discovered the electron?", 
     "1. J.J. Thomson", "2. Ernest Rutherford", "3. Niels Bohr", "4. James Chadwick", 1],

    ["Q66: What is the largest island country in the world?", 
     "1. Indonesia", "2. Madagascar", "3. Japan", "4. Philippines", 1],

    ["Q67: Who wrote 'The Hobbit'?", 
     "1. J.R.R. Tolkien", "2. C.S. Lewis", "3. J.K. Rowling", "4. George R.R. Martin", 1],

    ["Q68: What is the capital of Spain?", 
     "1. Barcelona", "2. Madrid", "3. Valencia", "4. Seville", 2],

    ["Q69: Who discovered the law of gravitation?", 
     "1. Isaac Newton", "2. Albert Einstein", "3. Galileo Galilei", "4. Johannes Kepler", 1],

    ["Q70: What is the largest coral reef system in the world?", 
     "1. Great Barrier Reef", "2. Belize Barrier Reef", "3. Red Sea Coral Reef", "4. New Caledonia Barrier Reef", 1],

    ["Q71: Who wrote 'The Picture of Dorian Gray'?", 
     "1. Oscar Wilde", "2. Charles Dickens", "3. Mark Twain", "4. F. Scott Fitzgerald", 1],

    ["Q72: What is the capital of Mexico?", 
     "1. Guadalajara", "2. Monterrey", "3. Tijuana", "4. Mexico City", 4],

    ["Q73: Who discovered the neutron?", 
     "1. James Chadwick", "2. Ernest Rutherford", "3. Niels Bohr", "4. J.J. Thomson", 1],

    ["Q74: What is the largest rainforest in the world?", 
     "1. Amazon Rainforest", "2. Congo Rainforest", "3. Daintree Rainforest", "4. Valdivian Temperate Rainforest", 1],

    ["Q75: Who wrote 'The Old Man and the Sea'?", 
     "1. Ernest Hemingway", "2. F. Scott Fitzgerald", "3. John Steinbeck", "4. J.D. Salinger", 1],

    ["Q76: What is the capital of Argentina?", 
     "1. Buenos Aires", "2. Córdoba", "3. Rosario", "4. Mendoza", 1],

    ["Q77: Who discovered the proton?", 
     "1. Ernest Rutherford", "2. J.J. Thomson", "3. Niels Bohr", "4. James Chadwick", 1],

    ["Q78: What is the largest desert in Africa?", 
     "1. Sahara Desert", "2. Kalahari Desert", "3. Namib Desert", "4. Libyan Desert", 1],

    ["Q79: Who wrote 'The Adventures of Tom Sawyer'?", 
     "1. Mark Twain", "2. Charles Dickens", "3. J.D. Salinger", "4. F. Scott Fitzgerald", 1],

    ["Q80: What is the capital of China?", 
     "1. Beijing", "2. Shanghai", "3. Guangzhou", "4. Shenzhen", 1],

    ["Q81: Who discovered the law of conservation of mass?", 
     "1. Antoine Lavoisier", "2. John Dalton", "3. Dmitri Mendeleev", "4. Robert Boyle", 1],

    ["Q82: What is the largest island in the Mediterranean Sea?", 
     "1. Sicily", "2. Sardinia", "3. Cyprus", "4. Crete", 1],

    ["Q83: Who wrote 'The Scarlet Letter'?", 
     "1. Nathaniel Hawthorne", "2. Herman Melville", "3. Edgar Allan Poe", "4. Mark Twain", 1],

    ["Q84: What is the capital of Turkey?", 
     "1. Istanbul", "2. Ankara", "3. Izmir", "4. Antalya", 2],

    ["Q85: Who discovered the circulation of blood?", 
     "1. William Harvey", "2. Andreas Vesalius", "3. Hippocrates", "4. Galen", 1],

    ["Q86: What is the largest lake in Africa?", 
     "1. Lake Victoria", "2. Lake Tanganyika", "3. Lake Malawi", "4. Lake Turkana", 1],

    ["Q87: Who wrote 'The Grapes of Wrath'?", 
     "1. John Steinbeck", "2. F. Scott Fitzgerald", "3. Ernest Hemingway", "4. J.D. Salinger", 1],

    ["Q88: What is the capital of Thailand?", 
     "1. Bangkok", "2. Phuket", "3. Chiang Mai", "4. Pattaya", 1],

    ["Q89: Who discovered the electron?", 
     "1. J.J. Thomson", "2. Ernest Rutherford", "3. Niels Bohr", "4. James Chadwick", 1],

    ["Q90: What is the largest island in the Caribbean?", 
     "1. Cuba", "2. Hispaniola", "3. Jamaica", "4. Puerto Rico", 1],

    ["Q91: Who wrote 'The Sun Also Rises'?", 
     "1. Ernest Hemingway", "2. F. Scott Fitzgerald", "3. John Steinbeck", "4. J.D. Salinger", 1],

    ["Q92: What is the capital of Greece?", 
     "1. Athens", "2. Thessaloniki", "3. Patras", "4. Heraklion", 1],

    ["Q93: Who discovered the law of universal gravitation?", 
     "1. Isaac Newton", "2. Albert Einstein", "3. Galileo Galilei", "4. Johannes Kepler", 1],

    ["Q94: What is the largest island in the Indian Ocean?", 
     "1. Madagascar", "2. Sri Lanka", "3. Maldives", "4. Seychelles", 1],

    ["Q95: Who wrote 'The Count of Monte Cristo'?", 
     "1. Alexandre Dumas", "2. Victor Hugo", "3. Jules Verne", "4. Honoré de Balzac", 1],

    ["Q96: What is the capital of Portugal?", 
     "1. Lisbon", "2. Porto", "3. Faro", "4. Coimbra", 1],

    ["Q97: Who discovered the law of definite proportions?", 
     "1. Joseph Proust", "2. John Dalton", "3. Antoine Lavoisier", "4. Robert Boyle", 1],

    ["Q98: What is the largest island in the Atlantic Ocean?", 
     "1. Greenland", "2. Iceland", "3. Newfoundland", "4. Bermuda", 1],

    ["Q99: Who wrote 'The Three Musketeers'?", 
     "1. Alexandre Dumas", "2. Victor Hugo", "3. Jules Verne", "4. Honoré de Balzac", 1],

    ["Q100: What is the capital of the United Kingdom?", 
     "1. London", "2. Edinburgh", "3. Cardiff", "4. Belfast", 1]
]

# List of prize levels for each question
prize_levels = [
    1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 
    160000, 320000, 640000, 1250000, 2500000, 5000000, 7500000, 
    10000000, 50000000, 70000000
]

# List of milestone indices where levels change
level_milestones = [8, 12, 15]  # Indices where levels change
milestone_prizes = [160000, 2500000, 10000000]  # Prizes for each milestone

total_won = 0
current_level = 0

# Function to play the game
def play_game():
    global total_won, current_level
    random.shuffle(questions)
    for index, question in enumerate(questions):
        print(f"Q{index + 1}: {question[0][4:]}")
        for i in range(1, 5):
            print(question[i])
        
        while True:
            if index == 0:
                answer = input("Please enter your option: ")
            else:
                answer = input("Please enter your option number or type 'quit' to exit: ") # Ask the user for an answer or to quit
            
            # Check if the user wants to quit the game
            if answer.lower() == 'quit':
                print(f"Congratulations, you have won Rs. {total_won}")
                return
            
            # Validate the user input
            try:
                answer = int(answer)
                if answer < 1 or answer > 4:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4, or type 'quit' to exit.")
        
        # Check if the answer is correct
        if answer != question[5]:
            print("Wrong answer! Game over.")
            if index > level_milestones[current_level]:
                total_won = milestone_prizes[current_level] 
            print(f"You have won Rs. {total_won}") # Print the total amount won
            break

        # If the answer is correct
        else:
            total_won = prize_levels[index]
            print("Correct answer!")
            if index < len(questions) - 1:
                print("Moving to the next question.")
            print(f"You have won Rs. {total_won}")
            # Check if the level has changed
            if index in level_milestones:
                current_level += 1

if __name__ == "__main__":
    play_game()