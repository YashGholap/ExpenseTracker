import flet as ft
from views import (
    login, 
    register, 
    dashboard
)

def main(page: ft.Page):
    
    def route_change(route):
        page.views.clear()
        
        if page.route ==  "/":
            page.views.append(login.LoginView(page))
        elif page.route == "/register":
            page.views.append(register.RegisterView(page))
        elif page.route == '/dashboard':
            page.views.append(dashboard.DashboardView(page))
            
            
        page.update()
        
    page.on_route_change = route_change
    page.go('/')
    
    
if __name__ == '__main__':
    ft.app(target=main)