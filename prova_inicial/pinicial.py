'''
Declare 3 variables that asks via stdin:
- An int between 1 - 10
- A value that is 0 or 1
- A text

Print via stdout these 3 variables separated by a comma
Make the following operations (these printed on console):
- 1st var. / 3
- 1st var. / 3 
- 1st var. % 3

Sixth part:
- 1st var AND 2nd var.
- 1st var OR 2nd var.
- 1st var AND 3rd var.
- 1st var. OR 3rd var. 
'''

def main() -> None:
    # First part
    try:
      num_1:int = int(input('Introdueix un nombre entre 1-10>'))
      num_2:int = int(input('Introdueix 0 o 1 >'))
      text_in:str = input('Escriu un text per la terminal>') 
    except:
        print('Error: invalid data type')
        exit()

    # Second part
    print(f"{num_1}, {num_2}, {text_in}")

    # Third part
    print(num_1 / 3)
    print(num_1 // 3)
    print(num_1 % 3)

    # No ha donat error, perque la funció int, converteix el input en un nombre enter
    
    # Sixth part

    print(num_1 and num_2)
    print(num_1 or num_2)
    print(num_1 and text_in)
    print(num_1 or text_in)

if __name__ == '__main__':
    main()
