import asyncio
from playwright.async_api import async_playwright

async def executar_robo_kamino(nome_cliente: str):
    print(f"[Robô Kamino] A iniciar sessão de automação para: {nome_cliente}")
    
    async with async_playwright() as p:
        # headless=False permite ver o navegador a abrir e a trabalhar sozinho
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        try:
            # Exemplo de navegação para o portal (substituir pela URL real de teste do Alessandro)
            await page.goto("https://sandbox.kamino.io")
            print(f"[Robô Kamino] Página carregada com sucesso para {nome_cliente}.")
            
            # Aqui entram os cliques automatizados de login e download do PDF...
            await asyncio.sleep(3)
            
        except Exception as e:
            print(f"[Erro no Robô] Ocorreu uma falha durante a execução: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(executar_robo_kamino("Cliente Exemplo Teste"))
