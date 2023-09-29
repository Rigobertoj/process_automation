dict1 = {
    "a" : {
        "a.1" : 1,
        "a.2" : 2
    },
    "b" : {
        "b.1" : 1,
        "b.2" : 2
    }

}

dict2 = {}

if __name__ == "__main__":
    dict2["a"] = dict1["a"]
    print(dict2.items())