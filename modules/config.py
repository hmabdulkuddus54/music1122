import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "19076488"))
API_HASH = getenv("API_HASH", "98e471abc04bd8febc1226d81ecef0c7")
BOT_TOKEN = getenv("BOT_TOKEN", "5433729660:AAGCd3-44Q7ANjTc9YaAlquaoCbVkaxz7q4")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "3000"))
STRING_SESSION = getenv("STRING_SESSION", "BQBc0eWTfg3zRHHadrBFBkMhtFch9WKeaepEHDy2X7X7fuqyGmGW9N76k_qxpvVvuToBYrt0KcO6xmAhKcf3jP2CoR98tE9udCl9aiREq-5gR_ENtU5XmMLGY9d-SLy1BNPw0JpEiSnEKWpthv6N_0sKMh2IoOISGpo4PtqEVhK0fWJgAoXFBKQMDs3OyeeUsHEdlyZOy0fjgln76nWTenTyHGmgXx4XmehGe3_Wl49emgT8EtMaQDcAhxLdLJz1crSck-ff5ASmveNCQsDBOKQnuF_IZgJ2f5fZfmr3oBQRL4tO6HpHLDFlN41VfB5uJAiQZK3HlCjwzbSdjCREkJLLAAAAATzTsGYA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5315473510").split()))
