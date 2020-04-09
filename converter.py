import os
import sys
import getopt


def convert(filename, target = "output.txt"):
    with open(filename,"r") as file:
        data = file.read()
        data = data.split(sep = "\n")
        print(data)
    result = ""
    i = 0
    while i<len(data):
        while i<len(data) and data[i]!="BEGIN:VCARD":
            i+=1
        if i!=len(data):
            i0 = i
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
            if data[i].startswith("CATEGORIES"):
                i+=1
            assert data[i].startswith("END:VCARD"),data[i0:i]
            result+="PROFILE:VCARD\n"
            result+=fullname + "\n"
            result+="N:;;;;\n"
            result+="REV:2020-04-09\n"
            if tel_bool:
                result+="TEL;TYPE=WORK,PREF:"+tel + "\n"
            result+="EMAIL;TYPE=INTERNET;TYPE=HOME;TYPE=PREF:"+mail + "\n"
            result+="END:VCARD\n"
            result+="\n"
    with open(target,"w") as file_tgt:
        file_tgt.write(result)
    print(result)

def test():
    convert(os.path.join("Exemple","exemple.txt"),os.path.join("Exemple","output.txt"))


if __name__ == "__main__":
    options, remainder = getopt.getopt(sys.argv[1:], "ti:o:",[])
    test_mode = False
    inp = None
    outp = None
    for opt, arg in options:
        if opt in ("-t"):
            test_mode = True
        elif opt in ("-i"):
            inp = arg
        elif opt in ("-o"):
            outp = arg

    if test_mode:
        test()
    else:
        if inp==None:
            inp = input("Entrez le nom du fichier à corvertir :")
        if outp == None:
            output = "output.vcs"
        convert(inp, outp)
