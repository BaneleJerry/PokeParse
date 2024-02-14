import csv

def main():
    file = 'pokemon.csv'

    cols = []
    rows = []

    with open(file , 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        
        cols = csvreader.fieldnames
        
        for row in csvreader:
            rows.append(row)
            
    options = ['1. Search by name',
               '2. Search by type',
               '3. List all pokemon known'
              ]
    for option in options:
        print(option)          
        
    option = input('Enter option: ')
    
    if option == '1':
        name = input('Enter pokemon name: ')
        pokemon = search_pokemon_by_name(rows, name)
        print(pokemon)
        if pokemon:
            print("Pokemon found:")
            for key, value in pokemon.items():
                print(f"{key}: {value}")
        else:
            print("Pokemon not found.")
            
            
    elif option == '2':
        type = input('Enter pokemon type: ')
        pokemon_ls = search_pokemon_by_type(rows,type)
        
        if pokemon_ls:
            print("Pokemon found:")
            for pokemon in pokemon_ls:
                print(format_output(cols, pokemon))
        else:
            print("Pokemon not found.")
        
    else:
        for row in rows:
            print(format_output(cols, row))
            

        

def search_pokemon_by_type(rows,type):
    results = []
    for row in rows:
        if row['Type 1'].lower() == type.lower() or row['Type 2'].lower() == type.lower():
            results.append(row)

    return results
    

def search_pokemon_by_name(rows, name):
    for row in rows:
        if row['Name'].lower() == name.lower():
            return row
    return None
    

def format_output(cols, pokemon):
    formatted_output = []
    for col in cols:
        formatted_output.append(f"{pokemon[col]}")
    return formatted_output

if __name__ == '__main__':
    main()
