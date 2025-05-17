import flet as ft
import asyncio
from services.api import register_user

class RegisterView(ft.View):
    
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.theme_mode = ft.ThemeMode.DARK
        
        self.username_field = ft.TextField(
            label = "Username",
            width= 300,
            prefix_icon=ft.Icons.PERSON,
            on_change = self.check_fields
        )
        self.email_field = ft.TextField(
            label="Email",
            width=300,
            prefix_icon=ft.Icons.EMAIL,
            on_change=self.check_fields
            )
        self.password_field = ft.TextField(
            label="Password",
            width=300,
            password=True,
            can_reveal_password=True,
            prefix_icon=ft.Icons.LOCK,
            on_change= self.check_fields
            )
        self.confirm_password_field = ft.TextField(
            label=" Confirm Password",
            width=300,
            password=True,
            can_reveal_password=True,
            prefix_icon=ft.Icons.LOCK_OUTLINE,
            on_change= self.check_fields
            )
        self.status_text = ft.Text("", color= ft.Colors.RED_400)
        self.register_button = ft.ElevatedButton(
            "Register",
            width= 100,
            height=50,
            disabled= True,
            on_click= self.register_handler
        )
        
        controls = [
            ft.Text("Register", size=30, weight="bold"),
            self.username_field,
            self.email_field,
            self.password_field,
            self.confirm_password_field,
            self.register_button,
            self.status_text,
            ft.Row([
                ft.Text("Already have an account?", size=18),
                ft.TextButton("Login", on_click= lambda e: self.page.go("/"))
            ], alignment=ft.MainAxisAlignment.CENTER)
        ]
        
        super().__init__(
            route="/register",
            controls= controls,
            horizontal_alignment="center",
            vertical_alignment="center"
        )
        
        
    def check_fields(self, e):
        username = self.username_field.value.strip()
        email = self.email_field.value.strip()
        password = self.password_field.value.strip()
        confirm_password = self.confirm_password_field.value.strip()
        
        if username and email and password and confirm_password:
            self.register_button.disabled = password != confirm_password
            if password != confirm_password:
                self.status_text.value = "Passwords do not match"
            else:
                self.status_text.value = ""
        else:
            self.register_button.disabled = True
            self.status_text.value = ""
        
        self.page.update()
        
    
    async def register_handler(self, e):
        username = self.username_field.value.strip()
        email = self.email_field.value.strip()
        password = self.password_field.value.strip()
        
        try:
            response = await register_user(username, email, password)
            if response.status_code == 200:
                self.page.snack_bar = ft.SnackBar(ft.Text("Registration successful! Redirecting to login....."))
                self.page.snack_bar.open = True
                self.page.update()
                
                await asyncio.sleep(3)
                self.page.go('/')
            else:
                self.status_text.value = response.json().get("detail", "Registration Failed")
                self.page.update()
                
        except Exception as e:
            self.status_text.value = f"Error: {str(e)}"
            self.page.update()
            
            
            
                    
            