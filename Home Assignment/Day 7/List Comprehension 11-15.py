square_list = [i ** 2 for i in range(1, 10+1)]
print(f"List of squares from 1 to 10 : {square_list}")


for num in range(1, 21):
    even_numbers = [num for num in range(1, 21) if num % 2 == 0]   
print("Even Numbers List:", even_numbers)


words = ["Apple", "banana", "Cherry"]
lower_list = [word.lower() for word in words]
print(f"Lower Case List : {lower_list}")


string = "python"
characters = [char for char in string]
print(f"Character :{characters}")



divisible_list = [num for num in range(1, 50+1) if num % 3 == 0 and num % 5 == 0]
print("Divisible List :", divisible_list)