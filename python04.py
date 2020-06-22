import xlrd
import pandas as pd
def get_data(z):
    dir_case = 'E:\\python-train\\' + z + '.xls'
    data = xlrd.open_workbook(dir_case)
    table = data.sheets()[0]
    nor = table.nrows
    nol = table.ncols
    
 
    list_1 = list()
    for i in range(1,nor):
        dict_1 = dict()
        for j in range(nol):
            title = table.cell_value(0,j)
            value = table.cell_value(i,j)
            dict_1[title] = value            
        list_1.append(dict_1)
 
 
    return list_1
 
if __name__ == '__main__':
    pf = get_data("三星體驗館地址")
    print(pd.DataFrame(pf))