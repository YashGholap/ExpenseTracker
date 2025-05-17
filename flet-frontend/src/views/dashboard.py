import flet as ft

class DashboardView(ft.View):
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.theme_mode = ft.ThemeMode.DARK
        
        self.user_email = self.page.session.get("user_email")
        self.username = self.user_email.split("@")[0].capitalize()
        
        self.expenses = []
        
        self.expense_table = ft.DataTable(
            visible=False,
            show_checkbox_column=True,
            columns=[
                ft.DataColumn(ft.Text("Date")),
                ft.DataColumn(ft.Text("Category")),
                ft.DataColumn(ft.Text("Amount")),
                ft.DataColumn(ft.Text("Note")),
            ],
            rows=[]
        )
        
        self.no_data_view = ft.Column(
            visible=True,
            controls=[
                ft.Text("You have no expenses.", italic=True),
                ft.TextButton("Add Expense", on_click=self.add_expense),
            ]
        )
        self.delete_button = ft.ElevatedButton(
            "Delete",
            icon = ft.Icons.DELETE,
            bgcolor=ft.Colors.RED_300,
            disabled=True,
            on_click= self.delete_selected_expenses
        )
        
        content = [
            ft.Row(
                alignment="spaceBetween",
                controls= [
                    ft.Text(f"Hey, {self.username}!", size=22, weight="bold"),
                    ft.IconButton(icon=ft.Icons.LOGOUT, tooltip="Logout", on_click=self.logout)
                ]
            ),
            ft.Divider(),
            ft.Container(
                content = ft.Text("Expense Chart Placeholder", size=18, italic=True),
                padding=20,
                bgcolor=ft.Colors.BLUE_50,
                border_radius=10,
                alignment = ft.Alignment(0.0,0.0),
            ),
            ft.Divider(),
            ft.Text("Your Expense", size=18,weight="w600"),
            self.no_data_view,
            self.expense_table,
            self.delete_button
        ]
        
        super().__init__(
            route="/dashboard",
            controls=content,
            horizontal_alignment="center",
            vertical_alignment="start",
            scroll=ft.ScrollMode.AUTO
        )
        
    
    async def did_mount_async(self):
        self.load_expenses()
        
    def logout(self, e):
        self.page.session.clear()
        self.page.go("/")
        
    def add_expense(self, e):
        self.page.go("/add-expense")
        
    def delete_selected_expenses(self, e):
        print("TODO: Implement delete login")
        
    def load_expenses(self):
        self.expenses = [
            {"date": "2025-05-01", "category": "Food", "amount": 200, "note": "Lunch"},
            {"date": "2025-05-02", "category": "Transport", "amount": 50, "note": "Bus ticket"}
        ]
        
        if self.expenses:
            self.expense_table.rows = [
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(exp["date"])),
                        ft.DataCell(ft.Text(exp["category"])),
                        ft.DataCell(ft.Text(str(exp["amount"]))),
                        ft.DataCell(ft.Text(exp["note"]))
                    ]
                ) for exp in self.expenses
            ]
            self.expense_table.visible =True
            self.no_data_view.visible = False
            self.delete_button.disabled = False
        else:
            self.expense_table.visible =False
            self.no_data_view.visible = True
            self.delete_button.disabled = True
            
        self.page.update()