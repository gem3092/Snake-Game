import csv

line_ct = 1


with open("/Users/indiv/Desktop/hl_ai_78.mrk", "r", encoding="utf8") as input_file:
    input_rdr = csv.reader(input_file)
    output_file = open("/Users/indiv/Desktop/hl_ai_78.csv", "w", encoding="utf8")

    for row in input_rdr:
        print(line_ct)
        x = "".join(row)
        output_file.write(x)
        output_file.write("\n")
        line_ct += 1


    input_file.close()
    output_file.close()
    print("Files closed.")

with open("/Users/indiv/Desktop/hl_ai_78.csv", "r", encoding="utf8") as input_file:
    input_rdr = csv.reader(input_file)
    output_file = open("/Users/indiv/Desktop/hl_ai_78_2.csv", "w", encoding="utf8")

    for row in input_rdr:
        x = " ".join(row)
        if "=001" in x:
            # output_file.write(x)
            # output_file.write("\n")
            mms_id = x
        if "(EXLNZ-01FALSC_NETWORK)" in x:
            nz = x
        if "$5" in x:
            output_file.write(str(mms_id))
            output_file.write(",")
            output_file.write(str(nz))
            output_file.write(",")
            fld = x.split(" ")
            output_file.write(fld[0])
            output_file.write(",")
            output_file.write(x)
            output_file.write(",")
            rhs = x.split("$5")
            for i in range(1, len(rhs)):
                output_file.write(str(rhs[i]))
                output_file.write(" ")
            output_file.write("\n")


    input_file.close()
    output_file.close()
    print("Files closed.")