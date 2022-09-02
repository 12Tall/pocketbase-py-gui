import os
import subprocess
import webview
import configparser


def parse_config():
    conf = configparser.ConfigParser()
    conf.read('config.ini')
    return {'port': conf['Server']['port']}


if __name__ == "__main__":
    conf = parse_config()
    executable = os.path.join(os.getcwd(), 'pocketbase/pocketbase.exe')

    si = subprocess.STARTUPINFO()
    # hide console
    # https://blog.csdn.net/ztb3214/article/details/19256849?utm_source=blogxgwz9
    si.dwFlags = subprocess.CREATE_NEW_CONSOLE | subprocess.STARTF_USESHOWWINDOW
    si.wShowWindow = subprocess.SW_HIDE
    pid = subprocess.Popen([executable, 'serve', '--http', '127.0.0.1:%s' %
                            conf['port']], close_fds=True, startupinfo=si)
    try:
        webview.create_window(title='pocketbase',
                              url='http://127.0.0.1:%s/_/' % conf['port'],
                              width=1200,
                              height=800)
        webview.start()
    except:
        pass
    finally:
        pid.kill()  # kill sub process automatically
