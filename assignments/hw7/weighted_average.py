"""
Name: <Aidan Riordan>
program name: <weighted_average>
I Aidan Riordan certify that this is my own work
"""

def main():
    #in_name = str(input("what is the in file name?"))
    #out_name = str(input("what is the out file name?"))
    #weighted_average(in_name, out_name)
    weighted_average("grades.txt", "out.txt")

def weighted_average(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w+")
    class_size = 0
    avg_acc = 0
    weight_acc = 0
    class_acc = 0
    for line in infile:
        new_line = line.split()
        for i in range(len(new_line), 2):
            avg = new_line[i] * new_line[i + 1]
            if(weight_acc > 100):
                outfile.write(name + "The weights are more than 100")


            elif(weight_acc<100):

                outfile.write(name + "The weights are less than 100")
            #class_size = class_size + 1
            #class_acc = class_acc + avg_acc

            else:
                list = line.split(":")
                name = list[0]
                g_and_w = list[1].split()

                # make 2 lists one with grades one with weights
                gs = []
                ws = []
                i = int(0)
                for val in g_and_w:
                    if i % 2 == 0:
                        ws.append(val)
                    else:
                        gs.append(val)
                    i = i + 1

                w_times_g_acc = 0
                i = 0
                for weight in ws:
                    w_times_g_acc = w_times_g_acc + int(ws[i]) * int(gs[i])
                    i = i + 1
                #print(w_times_g_acc)
                w_times_g_acc = w_times_g_acc / 100
                outfile.write(name + "'s average: " + str(w_times_g_acc) + "\n")


    outfile.close()
    infile.close()
if __name__ == '__main__':
    main()
