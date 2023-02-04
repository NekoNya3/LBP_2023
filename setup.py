import os 

rpms = [200, 350, 500]

for i in range(45):
    s = "" + str(i + 1).zfill(2) + "_" + str(rpms[i%3]) + "_S1_RE_F" + str(i // 9) + "_R" + str((( i//3 )%3) + 1)
    print(s)
    os.system('curl https://zenodo.org/record/3898942/files/'+ s +'.mat?download=1 --output Data/'+ s + '.mat')
