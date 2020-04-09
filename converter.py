def convert(filename, target = "output.txt"):
    with open(filename) as file:
        data = file.read(split = "\n")
    result = ""
    i = 0
    while i<=len(data):
        while i<=len(data) and data[i]!="BEGIN:VCARD":
            i+=1
        result+="BEGIN:VCARD\n"
        i+=1
        assert data[i]=="VERSION:3.0"
        result+="VERSION:3.0\n"
        i+=1
        assert data[i].startswith("FN:")
        fullname = data[i]
        i+=1
        assert data[i].startswith("N:")
        name = data[i]
        i+=1
        assert data[i].startswith("EMAIL")
        j = data[i].find(":")
        mail = data[i][j+1:]
        i+=1
        tel_bool = False
        if data[i].startswith("TEL"):
            j = data[i].find(":")
            tel = data[i][j+1:]
            tel_bool = True
            i+=1
        assert data[i].startswith("CATEGORIES")
        i+=1
        assert data[i].startswith("END:VCARD")
        result+="PROFILE:VCARD"
        result+=fullname + "\n"
        result+="N:;;;;\n"
        result+="REV:2020-04-09"
        if tel_bool:
            result+="TEL;TYPE=WORK,PREF:"+tel + "\n"
        result+="EMAIL;TYPE=INTERNET;TYPE=HOME;TYPE=PREF:"+mail + "\n"
        result+="END:VCARD"
    with open(target) as file_tgt:
        file_tgt.write(result)
    print(result)

convert(str(input()))
