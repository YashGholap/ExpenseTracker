import flet as ft
from views.login import LoginView
from views.register import RegisterView

def main(page: ft.Page):
    
    def route_change(route):
        page.views.clear()
        
        if page.route ==  "/":
            page.views.append(LoginView(page))
        elif page.route == "/register":
            page.views.append(RegisterView(page))
        # elif page.route == '/dashboard':
        #     page.views.append(dashboard_view(page))
            
            
        page.update()
        
    page.on_route_change = route_change
    page.go('/')
    
    
if __name__ == '__main__':
    ft.app(target=main)