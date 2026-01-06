import flet as ft
import random

# Lista de 10 países com bandeiras online
paises = [
    {"nome": "Austrália", "imagem": "https://flagcdn.com/w320/au.png"},
    {"nome": "Bélgica", "imagem": "https://flagcdn.com/w320/be.png"},
    {"nome": "Brasil", "imagem": "https://flagcdn.com/w320/br.png"},
    {"nome": "China", "imagem": "https://flagcdn.com/w320/cn.png"},
    {"nome": "Coreia do Sul", "imagem": "https://flagcdn.com/w320/kr.png"},
    {"nome": "Japão", "imagem": "https://flagcdn.com/w320/jp.png"},
    {"nome": "Cuba", "imagem": "https://flagcdn.com/w320/cu.png"},
    {"nome": "Alemanha", "imagem": "https://flagcdn.com/w320/de.png"},
    {"nome": "México", "imagem": "https://flagcdn.com/w320/mx.png"},
    {"nome": "África do Sul", "imagem": "https://flagcdn.com/w320/za.png"},
]

def main(page: ft.Page):
    page.bgcolor = ft.Colors.WHITE
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    page.window.width = 900
    page.window.height = 800

    total_niveis = len(paises)
    nivel_atual = 1

    # Copia da lista original para não repetir países
    paises_restantes = paises.copy()
    random.shuffle(paises_restantes)  # embaralha a ordem

    # Seleciona o primeiro país
    pais_atual = paises_restantes.pop()

    # Função para reconstruir o layout
    def build():
        nonlocal pais_atual, nivel_atual

        titulo = ft.Text(
            "🌍 Jogo das Bandeiras",
            size=20,
            weight="bold",
            color=ft.Colors.BLUE
        )

        nivel_text = ft.Text(
            f"Nível {nivel_atual} / {total_niveis}",
            size=14,
            color=ft.Colors.GREY
        )

        bandeira = ft.Container(
            expand=2,
            padding=30,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        "De qual país pertence esta bandeira?",
                        size=16,
                        color=ft.Colors.BLACK,
                        weight="bold"
                    ),
                    ft.Image(
                        src=pais_atual["imagem"],
                        width=350,
                        height=250,
                        
                    )
                ]
            )
        )

        answer_field = ft.TextField(
            label="Resposta",
            expand=True,
            text_size=12,
            border_radius=0,
            border_color=ft.Colors.BLACK,
            hint_text="Coloque o país aqui",
            on_submit=_on_submit,
            color=ft.Colors.BLACK,
        )

        resposta_container = ft.Container(
            expand=1,
            padding=30,
            content=answer_field
        )

        feedback_text = ft.Text(
            "Digite sua resposta e pressione Enter",
            size=16,
            color=ft.Colors.BLACK,
            weight="bold",
            expand=1
        )

        layout = ft.Container(
            padding=20,
            height=700,
            width=400,
            shadow=ft.BoxShadow(blur_radius=5, color=ft.Colors.BLACK),
            border_radius=ft.BorderRadius.all(10),
            bgcolor=ft.Colors.WHITE,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
                controls=[titulo, nivel_text, bandeira, resposta_container, feedback_text]
            )
        )

        page.controls.clear()
        page.add(layout)

        return answer_field, feedback_text, nivel_text

    # Função que processa a resposta do usuário
    def _on_submit(e):
        nonlocal nivel_atual, pais_atual, paises_restantes
        user_answer = e.control.value.strip().lower()

        if user_answer == pais_atual["nome"].lower():
            feedback.value = "✅ Correto!"
            nivel_atual += 1

            if nivel_atual > total_niveis:
                feedback.value = "🎉 Parabéns! Você completou o jogo."
                e.control.disabled = True
            else:
                # Pega o próximo país da lista embaralhada
                pais_atual = paises_restantes.pop()
                rebuild()
        else:
            feedback.value = "❌ Errado! Tente novamente."

        e.control.value = ""
        page.update()

    # Reconstrói o layout mantendo referências
    def rebuild():
        nonlocal answer_field, feedback, nivel_text
        answer_field, feedback, nivel_text = build()

    # Build inicial
    answer_field, feedback, nivel_text = build()

ft.app(target=main)
