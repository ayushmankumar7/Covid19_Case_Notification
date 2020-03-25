import win10toast

def admin_notify(x):
    n = win10toast.ToastNotifier()
    n.show_toast("Covid19 Update", f"{x}")
