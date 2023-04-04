import multiprocessing
from docx2pdf import convert

def con(name):
    convert(f"{name}.docx", f"{name}.pdf")

# con("About studying")
if __name__ == "__main__":

    multiprocessing.Process(target=con, args=(r"D:\LR BD new\Reports\About studying", )).start()

    for i in range(200000):
        print(i)
        