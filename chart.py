import matplotlib
import matplotlib.pyplot as plt
#避免中文乱码
matplotlib.rcParams['font.sans-serif']=['SimHei']
matplotlib.rcParams['axes.unicode_minus']=False

#显示饼图
def pie_chart(size,label,title):
    """
    绘制饼图
    size:各部分大小
    labels:设置各部分标签
    labeldistance:设置标签文本距圆心位置，1.1表示1.1倍半径
    autopct：设置圆里面文本
    shadow：设置是否有阴影
    startangle：起始角度，默认从0开始逆时针转
    pctdistance：设置圆内文本距圆心距离
    """
    plt.figure()    #图形画布
    plt.pie(size,labels=label,labeldistance=1.05,
            autopct='%1.1f%%',shadow=True,startangle=0,pctdistance=0.6)
    plt.axis('equal')       # 设置横轴和纵轴大小相等，这样饼才是圆的
    plt.title(title,fontsize=12)
    plt.legend(bbox_to_anchor=(0.03,1))     # 让图例生效，并设置图例显示位置
    plt.show()      #显示饼图



# 显示预测房价折线图
def broken_line(y,y_pred,title):
    '''
    y:y轴折线点，也就是房子总价
    y_pred,预测房价的折线点
    color：折线的颜色
    marker：折点的形状
    '''

    plt.figure()
    plt.plot(y,color='r',marker='o',label='真实房价')   # 绘制折线，并在折点添加蓝色圆点
    plt.plot(y_pred,color='b',marker='*',label='预测房价')
    plt.xlabel('房子数量')
    plt.ylabel('房子总价')
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()



#显示均价条形图
def average_price_bar(x,y,title):
    plt.figure()
    plt.bar(x,y,alpha=0.8)
    plt.xlabel('区域')
    plt.ylabel('均价')
    plt.title(title)
    #为每一个图形加数值标签
    for x,y in enumerate(y):
        plt.text(x,y+100,y,ha='center')
    plt.show()

#显示装修条形图
def renovation_bar(x,y,title):
    plt.figure()
    plt.bar(x,y,alpha=0.8)
    plt.xlabel('装修类型')
    plt.ylabel('数量')
    plt.title(title)
    #为每一个图形加数值标签
    for x,y in enumerate(y):
        plt.text(x,y+10,y,ha='center')
    plt.show()

#显示热门户型的水平条形图
def bar(price,type,title):
    """
    绘制水平条形图方法barh
    参数一：y轴
    参数二：x轴
    """
    plt.figure()
    plt.barh(type,price,height=0.3,color='r',alpha=0.8)
    plt.xlim(0,15000)
    plt.xlabel('均价')
    plt.title(title)
    #为每一个图像加数值标签
    for y,x in enumerate(price):
        plt.text(x+10,y,str(x)+'元',va='center')
    plt.show()





