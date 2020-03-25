import gi 
gi.require_version('Notify', '0.7')
from gi.repository import Notify

def sudo_notify(x):
    Notify.init("Covid19")
    msg = Notify.Notification.new("Covid19 Update", f"{x}")
    msg.show()