#Distance traveled calc.

while True:
    
    _distance = input("Travel Distance [ Km ]: ")
    _type = raw_input("Travel Type [ S, R, L ]: ")
    
    _S = 9.26
    _R = 12.964
    _L = 5.2

    print ((_distance) / (_S))/24.0 , "Days. Cost:", ((_distance) / (_R) / 24.0) * 17.0, "sp."
    print (_distance) / (_R) / 12.0 , "Days. Cost:", ((_distance) / (_R) / 12.0) * 12.0, "sp."
    print (_distance) / (_L) / 10.0 , "Days. Cost:", ((_distance) / (_R) / 10.0) * 4.0, "sp."

    print ""
