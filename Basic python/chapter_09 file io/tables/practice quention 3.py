#write a program to generate multiplication tables from 2 to 20 and write it in to the diffrent files.place these files in a folder for 13 year old child.
for i in range (1, 21):
        with open(f"tables/Multiplicaton table of {i}.txt", "w") as f:
                for j in range(1,11):
                          f.write(f"{i}X{j}={i*j}\n")

          
