from PyQt5.QtWidgets import QMainWindow,QApplication
from img.MainWindow import  Ui_MainWindow       #导入主窗体文件中的ui类
import sys                      # 导入系统模块
import house_analysis           # 导入自定义房子数据分析模块
import chart                    # 导入自定义绘图模块

#主窗体初始化类
class Main(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Main,self).__init__()
        self.setupUi(self)

    #显示各区二手房均价分析图
    def show_average_price(self):
        region, average_price=house_analysis.get_average_price()    # 获取房子区域与均价
        chart.average_price_bar(region,average_price,'各区二手房均价分析')

    # 显示各区二手房数量所占比例
    def show_house_number(self):
        region,percentage=house_analysis.get_house_number()
        chart.pie_chart(percentage,region,'各区二手房数量所占比例')

    # 显示全市二手房装修程度分析
    def show_renovation(self):
        type,number=house_analysis.get_renovation()
        chart.renovation_bar(type,number,'全市二手房装修程度分析')

    # 显示热门户型均价分析图
    def show_type(self):
        type,price=house_analysis.get_house_type()   # 获取全市二手房热门户型均价
        chart.bar(price,type,'热门户型均价分析')

    # 显示二手房售价预测折线图
    def show_total_price(self):
        true_price,forecast_price=house_analysis.get_price_forecast()   # 获取预测房价
        chart.broken_line(true_price,forecast_price,'二手房售价预测')      # 绘制及显示图表


if __name__=="__main__":
    app=QApplication(sys.argv)
    #主窗体对象
    main=Main()
    #显示各区二手房均价分析图，按钮事件
    main.btn_1.triggered.connect(main.show_average_price)
    # 显示各区二手房数量所占比例图，按钮事件
    main.btn_2.triggered.connect(main.show_house_number)
    # 显示全市二手房装修程度分析图，按钮事件
    main.btn_3.triggered.connect(main.show_renovation)
    # 显示热门户型均价分析图，按钮事件
    main.btn_4.triggered.connect(main.show_type)
    # 显示全市二手房户售价预测图，按钮事件
    main.btn_5.triggered.connect(main.show_total_price)
    #显示主窗体
    main.show()
    sys.exit(app.exec_())

