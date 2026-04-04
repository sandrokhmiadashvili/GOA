def yvelaze_grdzeli(list):
    grdzeli = list[0]
    
    for word in list:
        if len(word) > len(grdzeli):
            grdzeli = word
    
    return grdzeli
print(yvelaze_grdzeli(["cat", "elephant", "dog"]))  