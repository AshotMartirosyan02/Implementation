from hash_table import HashTable

if __name__ == "__main__":
    x = HashTable()


    x.put("brand", "Mercedes")
    x.put("electric", False)

    x.put("year", 2023)

    x.put("year", 2024)
    x.put("color", "black")

    print(x)
    x.remove("color")
    print(x)


    print(x.get("year"))
