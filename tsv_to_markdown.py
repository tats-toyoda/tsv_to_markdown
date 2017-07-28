
# coding: utf-8

# In[ ]:


import csv
from copy import deepcopy


# In[ ]:

l = input().split()
input_file = 'input/' + l[2]
output_file = 'output/' + l[3]


# In[ ]:

def insert(list_input):
    """
    listの先頭と末尾に空の要素を追加する.
    """
    list_output = deepcopy(list_input) # 値渡しでlistをコピー
    len_ = len(list_output)
    list_output.insert(len_, '')
    list_output.insert(0, '')
    return list_output


# In[ ]:

list_ = []
with open(input_file) as f_open:
    tsv_reader = csv.reader(f_open, delimiter='\t')
    fieldname = tsv_reader.__next__()
    column_length = len(fieldname)
    #print(fieldname)
    for row in tsv_reader:
        list_.append(insert(row))
    sep = list()
    for i in range(column_length):
        sep.append(':-----:')
    list_.insert(0, insert(sep))


# In[ ]:

with open(output_file, 'w') as f_write:
    markdown_writer = csv.writer(f_write, delimiter='|', lineterminator='\n')
    markdown_writer.writerow(insert(fieldname))
    for row in list_:
        markdown_writer.writerow(row)

