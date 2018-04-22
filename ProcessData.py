import pandas as pd 
#https://archive.ics.uci.edu/ml/datasets/adult
data =pd.read_csv("adult.csv")
data.info()

''' process unknow data '''
colx = data.columns

for c in colx:
    nox = data[c].isin(['?']).sum()
    print (nox, " ",c )
    '''it count ? in the dataframe 
        and i can see 
            2799 workclass 
            2809   occupation
            857   native-country
    '''

# ingone the "?" 
data = data[data['workclass']!= '?']
data = data[data['occupation']!= '?']
data = data[data['native-country']!= '?']

# data we have a complete table but cant use yet 
''' to train this data we have to change info to number '''
# https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.names
'''
workclass : lớp công việc 
    private = tư nhân 
    Self-emp-not-inc = tự làm việc không có nguồn thu 
    Self-emp-inc = tự làm việc có nguồn thu  
    Federal-gov = chính phủ liên bang 
    Local-gov = chính quyền địa phương 
    State-gov = chính quyền bang 
    Without-pay = làm không công 
    Never-worked = thất nghiệp 
education: tên trường học không dịch đươc 
    Bachelors,
    Some-college, 
    11th, HS-grad, 
    ...
marital-status: 
    Married-civ-spouse = đã kết hôn 
    Divorced = ly hôn 
    Never-married = không bao h kết hôn 
    Separated = ly thân 
    Widowed = góa vợ/chồng 
    Married-spouse-absent = ế 
    Married-AF-spouse = đã kết hôn 
occupation: nghề nghiệp 
    Tech-support = hổ trợ kỷ thuật 
    Craft-repair = sử chửa thủ công 
    Other-service = dịch vụ 
    Sales = bán hàng 
    Exec-managerial = quản lí thi công 
    Prof-specialty =chuyên môn nghiệp vụ 
    Handlers-cleaners = xử lý chất tẩy 
    Machine-op-inspct
    Adm-clerical, 
    Farming-fishing =nuôi cá 
    Transport-moving = vận chuyển  
    Priv-house-serv = osin  
    Protective-serv = bảo vệ 
    Armed-Forces = quân nhân 
relationship :
    Wife = vợ
    Own-child = có con riêng
    Husband = chồng 
    Not-in-family = không trong gia đình 
    Other-relative = người thân khác 
    Unmarried = chưa cưới 
race : màu da 
    White = trắng
    Asian-Pac-Islander = châu á thái bình dương  
    Amer-Indian-Eskimo = châu mỹ - ấn 
    Other = khác 
    Black = đen 
native-country: quốc gia
    United-States, 
    Cambodia, 
    England,
    ...

kết quả trả về : >50K, <=50K.
'''