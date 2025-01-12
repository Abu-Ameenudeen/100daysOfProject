def main():
    print("Welcome to the Band Name Generator.")
    city = input("What's the name of the city you grew up in?\n")
    pet_name = input("What's your pet's name?\n")
    output = generate_band_name(city, pet_name)
    print("")
    print(output)
    

def generate_band_name(city_name, pet_name):
    return f"Your band name could be {city_name} {pet_name}"

    
if __name__ == "__main__":
    main()
