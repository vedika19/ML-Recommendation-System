import wx
import Main1
from Main1 import rec





class ExamplePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.quote = wx.StaticText(self, label="RECOMMENDATION SYSTEM", pos=(50, 30))

        # A multiline TextCtrl - This is here to show how the events work in this program, don't pay too much attention to it
        self.logger = wx.TextCtrl(self, pos=(300,20), size=(200,300), style=wx.TE_MULTILINE | wx.TE_READONLY)

        # A button
        self.button =wx.Button(self, label="Find recommendation", pos=(200, 325))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)

        # the edit control - one line version.
        self.lblname = wx.StaticText(self, label="Enter USERID :", pos=(20,60))
        self.editname = wx.TextCtrl(self, value="", pos=(150, 60), size=(140,-1))
        self.Bind(wx.EVT_TEXT, self.OnClick, self.button)
        self.Bind(wx.EVT_CHAR, self.EvtChar, self.editname)


    def EvtRadioBox(self, event):
        self.logger.AppendText('EvtRadioBox: %d\n' % event.GetInt())
    def EvtComboBox(self, event):
        self.logger.AppendText('EvtComboBox: %s\n' % event.GetString())
    def OnClick(self,event):
    	#self.result.SetLabel(self.editname.GetValue())
    	#self.logger.AppendText(self.editname.GetValue())
    	#result=Brain.recom(self.editname.GetValue())
        self.logger.SetValue("")
    	print self.editname.GetValue()

        result=Main1.rec(self.editname.GetValue())
            
        
        

        self.logger.AppendText(result)
    	
    #def OnPopupItemSelected(self, event):
        
        #Main1.rec()
    	#print result
    	#for i in result:
    	#	self.logger.AppendText(i)
        #self.logger.AppendText(" Click on object with Id %d\n" %event.GetId())
    def EvtText(self, event):
        item = self.popupmenu.FindItemById(event.GetId())
        text = editname.GetText()
        wx.MessageBox("Invalid User Id" )
    def EvtChar(self, event):
        self.logger.AppendText('EvtChar: %d\n' % event.GetKeyCode())
        event.Skip()
    def EvtCheckBox(self, event):
        self.logger.AppendText('EvtCheckBox: %d\n' % event.Checked())


app = wx.App(False)
frame = wx.Frame(None)
panel = ExamplePanel(frame)
frame.Show()
app.MainLoop()