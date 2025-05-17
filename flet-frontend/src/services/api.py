import httpx


BASE_URL = "http://localhost:8000"

async def login_user(email: str, password: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BASE_URL}/auth/login",
            json={"email": email, "password": password}
        )
        return response
    
async def register_user(username: str, email: str, password: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BASE_URL}/auth/register",
            json={
                "username": username,
                "email": email,
                "password": password
            }
        )
        return response