html_tags=['<html>','<title>','<body>','<span>','<img>','<a>','<p>','<div>','<h>'
          ,'</h>','</div>','</p> ','</a>','</img>','</span>','<body>','</title>','</html>']

tags=['<','/','>']

dictionary={'<html>':'</html>','<body>':'</body>','<a>':'</a>','<p>':'</p> ','<div>':'</div>','<h>':'</h>','<>':'</>',
            '<img>':'</img>','<title>':'</title>','<span>':'</span>','<table>':'</table>',
             '<tbody>':'</tbody>','<strong>':'</strong>','<script>':'</script>'}

with open('C:/Users/DELL/Desktop/eka.html','r')as file:
    read_lines=[]
    for lines in file.readlines():  #reading the html tags from an html file
        create_new_line=[]
        for alphabets in lines:
            create_new_line.append(alphabets)
        read_lines.append(create_new_line)

reserve=[]               #storing each string in the reserve list
length=len(read_lines)
for str in range (length):
    for j in read_lines[str]:
        h=''.join(read_lines[str])
    reserve.append(h)

new_list = [s.replace("\n", "") for s in reserve]   #replacing the new lines with space to split them at space
print(new_list)

holla=[]
for tag1 in html_tags:
    for tag2 in new_list:         # saving elements  in new list which are found in html tag list and removing them from the former list
        if tag1==tag2:
            holla.append(tag2)
            new_list.pop(new_list.index(tag2))
print(holla)

reserve2=[]    #crearing a new list to store the remaining tags
for rem_tags in  new_list:
    reserve2+=new_list[new_list.index(rem_tags)]  #changing the string list to list of characters to extract the remaining tags

store3=[]
for rem_tag2 in reserve2:
    for j in tags:
        if rem_tag2==j:
            store3.append(rem_tag2)
        if rem_tag2=='>':
            store3.append(reserve2[reserve2.index(rem_tag2)-1])
                                                                        #print(store3)

store4=[]
for rem_tag3 in store3:
    for reference_tag in tags:
        if rem_tag3==reference_tag:
            store4.append(rem_tag3)
#print(store4)

array1=[]
for tag5 in holla:
    if tag5 in dictionary: # checking the tags extracted from the html with reference to the dictioary
        array1.append(tag5)
    else:
        if len(array1) == 0:
            print('Invalid')       #removing the tags by checking with reference to keys and values foung in dictionary
            break;
        if dictionary[array1[-1]]== tag5:
            array1.pop(-1)
        else:
            print('Invalid')
            break;

store5=[]   #creating another list to store the syntaxes
store6=[' '] #creating another list with empty sppace to divide the charaters with space so that it would become easier to split
for tag6 in store4:
    if tag6 =='>':
        store5.append(tag6)
        store5.append(store6[0])
    else:
        store5.append(tag6)
joined_str=''.join(store5)

splitted_str=joined_str.split(" ")

while("" in splitted_str) :   #removing empty charatcers fron the list
    splitted_str.remove("")
print(splitted_str," the remaining tags from the strings")

list=[]
for tag7 in splitted_str:
    if tag7 in dictionary:
        list.append(tag7)
    else:
        if len(list) == 0:
            print('Invalid')
            break;
        if dictionary[list[-1]]== tag7:
            list.pop(-1)
        else:
            print('Invalid')
            break;
if len(list) == 0 and len(array1) == 0 and splitted_str[len(splitted_str)-1]!='<>':
    print('valid')
else:
    print('invalid')