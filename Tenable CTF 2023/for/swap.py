x = open("out.bin", "wb")

with open("lost_evidence", "rb") as f:
    while(data := f.read(2)):
        x.write(data[::-1])