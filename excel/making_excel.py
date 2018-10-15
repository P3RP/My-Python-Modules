# -*- coding:utf-8 -*-


# Example of basic format
def make_excel(dataList):
    """
        :호출예시 make_excel([ [1,2,3,4], [5,6,7,8] ]) or make_excel(2dArray)
        :param dataList:  [ data1, data2, data3, data4 ] 꼴의 1차원 list를 가지는 2차원 list
        :return: 없
    """
    # === CONFIG
    FILENAME = "엔카.xlsx"

    # === SAVE EXCEL
    wb = Workbook()
    ws1 = wb.worksheets[0]
    header1 = ['제조사', '모델', '세부모델', '등급']
    ws1.column_dimensions['A'].width = 30
    ws1.column_dimensions['B'].width = 30
    ws1.column_dimensions['C'].width = 50
    ws1.column_dimensions['D'].width = 50
    ws1.append(header1)
    # data save

    for data in dataList:
        ws1.append(data)
    # end
    wb.save(FILENAME)


# Example for merging cells
def make_excel_2(data_list, name):
    """
        :호출예시 make_excel([ [1,2,3,4], [5,6,7,8] ]) or make_excel(2dArray)
        :param data_list:  [ data1, data2, data3, data4 ] 꼴의 1차원 list를 가지는 2차원 list
        :return: 없
    """
    # === CONFIG
    FILENAME = name + ".xlsx"

    # === SAVE EXCEL
    wb = Workbook()
    ws1 = wb.worksheets[0]
    header1 = ['(보고서 번호) 회사 / 보고서 제목', '보고사유', '변동일*', '특정증권등의 종류', '소 유 주 식 수 (주)', '', '',
               '취득/처분 단가(원)**', '비고']
    header2 = ['', '', '', '', '변동전', '증감', '변동후', '', '', '']
    ws1.column_dimensions['A'].width = 50
    ws1.column_dimensions['B'].width = 30
    ws1.column_dimensions['C'].width = 20
    ws1.column_dimensions['D'].width = 20
    ws1.column_dimensions['E'].width = 20
    ws1.column_dimensions['F'].width = 20
    ws1.column_dimensions['G'].width = 20
    ws1.column_dimensions['H'].width = 20
    ws1.column_dimensions['I'].width = 20
    ws1.append(header1)
    ws1.append(header2)

    ws1.merge_cells('A1:A2')
    ws1.merge_cells('B1:B2')
    ws1.merge_cells('C1:C2')
    ws1.merge_cells('D1:D2')
    ws1.merge_cells('E1:G1')
    ws1.merge_cells('H1:H2')
    ws1.merge_cells('I1:I2')

    header_cell_list = ['A1', 'B1', 'C1', 'D1', 'E1', 'E2', 'F2', 'G2', 'H1', 'I1']
    for cell in header_cell_list:
        cal = ws1[cell]
        cal.alignment = Alignment(horizontal='center', vertical='center')

    # DATA SAVE
    for comment_data in data_list:
        ws1.append(comment_data)
    # END
    wb.save(FILENAME)
