import SMSService

import wpf

from System.Windows import Application, Window, MessageBox
import System.Windows


class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'MainWindow.xaml')
        self.sm = SMSService.SMSService()
    
    

    
    def btnSend_Click(self, sender, e):
        try:
            self.sm.sendSurvay(self.tbxMobile.Text,"客户")
        except Exception as e:
            MessageBox.Show("短信接口错误：{0}".format(e.message))
            return
        MessageBox.Show('调查信息已发送，谢谢您的参与！',"信息")

        self.tbxMobile.Text = ""
        pass
    

if __name__ == '__main__':
    Application().Run(MyWindow())
