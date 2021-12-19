from common_practice.autofunc.Keys import Key

web = Key('Chrome')
web.open_url('http://www.baidu.com')
web.input_txt('id', 'kw', '东旭为什么这么帅')
web.clicker('id', 'su')
web.wait(30)
web.quit()
