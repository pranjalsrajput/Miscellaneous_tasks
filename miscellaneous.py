def convertDataToQnAFormat():
    import pandas as pd
    from pandas import DataFrame, read_csv
    import xlsxwriter

    dataframe = pd.read_excel(r"/home/pranjal/Documents/Assignments/DeepLearning/TA/Q&A/Paper 10 On Empirical Comparisons of Optimizers for Deep Learning_2020-3-22_20-57-16/Paper 10 On Empirical Comparisons of Optimizers for Deep Learning_2020-3-22_20-57-16.xlsx", sheet_name="1FPS")
    print(dataframe["FRAME NO"].unique())
    # ls=dataframe["FRAME NO"].unique()
    # print(len(ls))

    row_no=0
    col_no=0
    workbook=xlsxwriter.Workbook("Paper 10 On Empirical Comparisons of Optimizers.xlsx")
    worksheet= workbook.add_worksheet("Questions&Answers")
    i=0

    for index, row in dataframe.iterrows():
        row_no += 1
        i+=1
        col_no = 0
        print("Student Number: ", row["Student Number"])
        print("Question: ", row["Question"])
        print("Option A: ", row["Option A"])
        print("Option B: ", row["Option B"])
        print("Option C: ", row["Option C"])
        print("Option D: ", row["Option D"])
        print("Answer: ", row["Answer"])
        print(" ")
        worksheet.write(row_no, col_no, "Student Number")
        worksheet.write(row_no, col_no+1, str(row["Student Number"]))
        row_no += 1
        worksheet.write(row_no, col_no, "Question "+str(i))
        worksheet.write(row_no, col_no+1, str(row["Question"]))
        row_no += 1
        worksheet.write(row_no, col_no, "Option A")
        worksheet.write(row_no, col_no+1, str(row["Option A"]))
        row_no += 1
        worksheet.write(row_no, col_no, "Option B")
        worksheet.write(row_no, col_no+1, str(row["Option B"]))
        row_no += 1
        worksheet.write(row_no, col_no, "Option C")
        worksheet.write(row_no, col_no+1, str(row["Option C"]))
        row_no += 1
        worksheet.write(row_no, col_no, "Option D")
        worksheet.write(row_no, col_no+1, str(row["Option D"]))
        row_no += 1
        worksheet.write(row_no, col_no, "Answer")
        worksheet.write(row_no, col_no+1, str(row["Answer"]))
        row_no += 1
        # finish_time = row["cumulativeTime_finish"]

    workbook.close()

def mergePDFS():
    import PyPDF2
    from io import BytesIO

    pdfs = ['/home/pranjal/Documents/Assignments/Deep Learning Project/Project Proposal/Project Proposal.pdf', '/home/pranjal/Documents/Assignments/Deep Learning Project/Report/Eindhoven Marathon Dataset Collection and Analysis Report.pdf']
    writer = PyPDF2.PdfFileWriter()
    tmp = BytesIO()
    path = open('/home/pranjal/Documents/Assignments/Deep Learning Project/Project Proposal/Project Proposal.pdf', 'rb')
    path2 = open('/home/pranjal/Documents/Assignments/Deep Learning Project/Report/Eindhoven Marathon Dataset Collection and Analysis Report.pdf', 'rb')
    merger = PyPDF2.PdfFileMerger()
    merger.append(fileobj=path2)
    merger.append(fileobj=path)
    merger.write(tmp)
    PyPDF2.filters.compress(tmp.getvalue())
    merger.write(open("test_out2.pdf", 'wb'))

def convertXLToJson():
    import pandas
    import json

    excel_data_fragment = pandas.read_excel('./Final_Timeline.xlsx')
    json_str = excel_data_fragment.to_json(orient='records')
    #print('Excel Sheet to JSON:\n', json_str)
    with open('Final_Timeline.json', 'w') as f:
        json.dump(json_str, f)

def rotate_img(img_path, rt_degr):
    from PIL import Image
    img = Image.open(img_path)
    return img.rotate(rt_degr, expand=1)

if __name__ == "__main__":
    convertXLToJson()
    ##### Image rotation #####
    # path_to_images = '/home/pranjal/Documents/PythonProjects/SampleDataset/2_card_nearby_Location_10/Frames/VID_20191013_104456_2/'
    # for filename in glob.glob(os.path.join(path_to_images, '*.jpg')):
    #     img_rt_90 = rotate_img(filename, 180)
    #     img_rt_90.save(filename)
