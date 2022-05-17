# Author: Daniel Lee


def getIDs(filename):
    id_list=[]
    sales_data=[]
    file=open(filename,'r')
    for line in file:
        id_list.append(line.strip())
        sales_data.append([0.00,0.00,0.00,0.00])
    file.close()
    return id_list,sales_data


def process_sales_data(filename, id_list, sales_data):
    file=open(filename,'r')
    for line in file:
        line=line.strip().split()
        ids=line[0]
        val=int(line[1])
        if val>=1 and val<=3:
            qtr=0
        elif val>=4 and val<=6:
            qtr=1
        elif val>=6 and val<=9:
            qtr=2
        else:
            qtr=3

        amount=float(line[2])
        loc=id_list.index(ids)
        sales_data[loc][qtr]=round((sales_data[loc][qtr]+amount),2)
    file.close()
    return sales_data  

# figuring out the quratiles values for each ID
def print_report(id_list, sales_data):
    print('\n  -------Annual Sales Report------\n')
    print('{:<10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format('ID','QT1','QT2','QT3','QT4','Total'))
    """if :
        print("0.00")"""
    qtr1=0
    qtr2=0
    qtr3=0
    qtr4=0
    max_id=0
    max_value=0
    for i in range(len(id_list)):
        qtr1=qtr1+sales_data[i][0]
        qtr2=qtr2+sales_data[i][1]
        qtr3=qtr3+sales_data[i][2]
        qtr4=qtr4+sales_data[i][3]
        total=round(sum(sales_data[i]),2)
        value=max([sales_data[i][0],sales_data[i][1],sales_data[i][2],sales_data[i][3]])
        if value>max_value:
            max_value=value
            max_id=id_list[i]
        print('{:<8}{:>10}{:>10}{:>10}{:>10}{:>10}'.format(id_list[i],sales_data[i][0],sales_data[i][1],sales_data[i][2],sales_data[i][3],total))
    qtr_total=qtr1+qtr2+qtr3+qtr4
    print('{:<8}{:>10}{:>10}{:>10}{:>10}{:>10}'.format('Total',round(qtr1,2),round(qtr2,2),round(qtr3,2),round(qtr4,2),round(qtr_total,2)))
    amount=max([qtr1,qtr2,qtr3,qtr4])
    loc = [qtr1,qtr2,qtr3,qtr4].index(amount)
    print('\nMax sales by Salesperson: ID =',max_id+', Amount = $'+str(round(max_value,2)))
    print('Max sales by Quarter: Quarter = ',str(loc+1)+', Amount = $'+str(round(amount,2)))

# Asking for the name of the files
def main():
    id_file_name=input('Enter the name of the sales ids file: ')
    id_list, sales_data=getIDs(id_file_name)
    data_file_name=input('Enter the name of the sales data file: ')
    sales_data=process_sales_data(data_file_name, id_list, sales_data)
    print_report(id_list,sales_data)

main()
