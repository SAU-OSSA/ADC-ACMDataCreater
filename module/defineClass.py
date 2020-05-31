
#储存全部全局的变量
global var
var = {} 

#得到值 & 赋值
def val(name,value = 'no1215_'):
    if value != 'no1215_':
        var[name] = value
    try:
        return var[name]
    except:
        return None

#log全局变量
def log(name):                   
    try:
        print('log{'+name+':'+str(var[name])+'}')
    except:
        print('log{'+name+':None}')

