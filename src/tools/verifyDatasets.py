# import glob
# print(glob.glob("D:/Git_WorkSpace/ITSEC21/data/FingerPrints/test/*.jpeg"))


import os

F_Test = os.listdir('D:/Git_WorkSpace/ITSEC21/data/FingerPrints/test')
F_Train = os.listdir('D:/Git_WorkSpace/ITSEC21/data/FingerPrints/train')
F_Valid = os.listdir('D:/Git_WorkSpace/ITSEC21/data/FingerPrints/val')

M_Test = os.listdir('D:/Git_WorkSpace/ITSEC21/data/Minutiae_Maps/test')
M_Train = os.listdir('D:/Git_WorkSpace/ITSEC21/data/Minutiae_Maps/train')
M_Valid = os.listdir('D:/Git_WorkSpace/ITSEC21/data/Minutiae_Maps/val')


F_Test_New = [s.replace(".jpeg", "") for s in F_Test]
F_Train_New = [s.replace(".jpeg", "") for s in F_Train]
F_Valid_New = [s.replace(".jpeg", "") for s in F_Valid]

M_Test_New = [s.replace(".png", "") for s in M_Test]
M_Train_New = [s.replace(".png", "") for s in M_Train]
M_Valid_New = [s.replace(".png", "") for s in M_Valid]

print("F Test length: ", len(F_Test_New), " M Test length: ", len(M_Test_New))
print("F Train length: ", len(F_Train_New), " M Train length: ", len(M_Train_New))
print("F Val length: ", len(F_Valid_New), " M Val length: ", len(M_Valid_New))

if F_Test_New == M_Test_New:
    print("Test data is identical")
else :
    print("Test data is not identical")

if F_Train_New == M_Train_New:
    print("Train data is identical")
else :
    print("Train data is not identical")

if F_Valid_New == M_Valid_New:
    print("Validation data is identical")
else :
    print("Validation data is not identical")