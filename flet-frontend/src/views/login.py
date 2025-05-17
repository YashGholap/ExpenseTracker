import flet as ft
from services.api import login_user


class LoginView(ft.View):
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.theme_mode = ft.ThemeMode.DARK
        
        self.email_field = ft.TextField(label="Email", width= 300, on_change= self.check_fields)
        self.password_field = ft.TextField(label="Password",width=300, password=True, can_reveal_password=True, on_change= self.check_fields)
        self.status_text = ft.Text("", color=ft.Colors.RED_400)
        
        self.login_button = ft.ElevatedButton("Login",disabled=True ,on_click= self.login_handler,
                                         width=100,
                                         height=50
                                         )
        
        controls = [
            ft.Text("Welcome to Expense Tracker", size=30, weight="bold"),
            self.email_field,
            self.password_field,
            ft.Row([
                ft.Text("New here?", size=18),
                ft.TextButton("Register now",
                              on_click=lambda e: self.page.go("/register"),
                              style=ft.ButtonStyle(color=ft.Colors.BLUE_400))
            ], alignment= ft.MainAxisAlignment.CENTER),
            self.login_button,
            self.status_text
        ]
        
        super().__init__(
            route="/",
            controls= controls,
            horizontal_alignment= "center",
            vertical_alignment="center"
        )
        
        
    def check_fields(self, e):
        email = self.email_field.value.strip()
        password = self.password_field.value.strip()
        self.login_button.disabled = not(email and password)
        self.page.update()
    
    async def login_handler(self, e):
        email = self.email_field.value
        password = self.password_field.value
        
        if not email or not password:
            
            self.status_text.value = "Email and Password are required."
            self.page.update()
            return
        
        try:
            response = await login_user(email, password)
            
            if response.status_code == 200:
                token = response.json().get("access_token")
                self.page.session.set("token",token)
                self.page.go("/dashboard")
            else:
                self.status_text.value = "Invalid Credentials"
                self.page.update()
                
        except Exception as e:
            self.status_text.value = f"Error: {str(e)}"
            self.page.update()
            
