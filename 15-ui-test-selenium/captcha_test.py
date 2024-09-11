from seleniumbase import SB

# with SB(uc=True, test=True) as sb:
#     # url = "https://gitlab.com/users/sign_in"
#     url = "https://dash.cloudflare.com/login"
#     sb.uc_open_with_reconnect(url, 4)
#     sb.uc_gui_click_captcha()
#     sb.sleep(5)

with SB(uc=True, test=True) as sb:
    sb.uc_open_with_reconnect(url, 4)
    sb.click("#header-login")
    sb.click("#link_forget")
    sb.click(".tab-primary-box li:nth-of-type(2) a")
    sb.uc_gui_click_captcha()
    sb.sleep(5)
